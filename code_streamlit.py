# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 14:09:02 2023

@author: DUQUEYROIX
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MaxAbsScaler
from sklearn.preprocessing import OneHotEncoder


def accueil():
    title_style = "color: red; text-align: center;"
    st.markdown(f"<h1 style='{title_style}'>Temps de Réponse de la Brigade des Pompiers de Londres</h1>", unsafe_allow_html=True)
    st.image('./firetruck.jpg')
    
def presentation():
    st.write("### Présentation")
    
    st.write("Dans le cadre de notre projet de formation, nous nous sommes intéressés au temps de réponse de la Brigade des Pompiers de Londres.")
    st.image("./LFB.png")
    st.write("La brigade des pompiers de Londres, aussi appelée London Fire Brigade, est le cinquième plus grand corps de sapeurs-pompiers dans le monde avec plus de 5 096 sapeurs-pompiers professionnels et 103 casernes. Ils interviennent dans les 33 'boroughs',  subdivision administrative de Londres. ")
    st.write("Leur rôle dans la ville est important. La brigade des pompiers, par leurs interventions rapides, permet à de nombreuses vies d'être sauvées, des édifices préservés, des milieux naturels sauvegardés.")
    st.write("L'objectif de notre travail va être d'analyser leur temps de réponse et de prédire en combien de temps les pompiers pourront arriver sur les lieux de l'accident suivant différents paramètres. Ces résultats pourront servir de base au service des pompiers afin d'être plus réactif et d'améliorer leur temps de réponse.")


def jeudedonnee():
    title_style = "color: red;"  # Style CSS pour la couleur rouge
    st.write("### Exploration des données")
    st.markdown(f"<h4 style='{title_style}'>Données clés</h4>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)  # Vous pouvez aussi utiliser st.columns()
    col1.write("942 502  incidents entre 2017 et 2022")
    col2.write(" 3 types d'incidents : Feux, Fausse alarme et Service Special")
    col3.write("Intervention sur les 33 'boroughs' de Londres")
    
    st.markdown(f"<h4 style='{title_style}'>Travaux préparatoires</h4>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)  # Vous pouvez aussi utiliser st.columns()
    col1.write("**Importation des datasets**")
    col1.write("2 datasets : 1 contenant les détails de chaque incident traité et l'autre les détails de chaque camion de pompiers envoyé sur les lieux ")
    col1.write("Disponible librement sur le [site des pompiers de Londres](https://data.london.gov.uk/dataset/london-fire-brigade-incident-records)")
    col2.write("**Vérification des données**")
    col2.write("Fusion des deux Dataframes")
    col2.write("Vérification et correction du format des données")
    col3.write("**Nettoyage des données**")
    col3.write("Suppression des colonnes inutiles au projet")
    col3.write("Suppression des valeurs manquantes")
      
    st.markdown(f"<h4 style='{title_style}'>Ajout de données d'intérêt </h4>", unsafe_allow_html=True)
    st.write("• Ajout de la localisation des casernes (latitude, longitude et adresse")
    st.write("• Calcul de la latitude et de la longitude pour localiser les incidents")
    st.write("• Calcul de la distance entre la caserne et le lieu de l'incident")
    
    st.markdown("<h9>Aperçu du Dataframe:</h9>", unsafe_allow_html=True)
    pompier = pd.read_csv("pompier.csv")
    st.dataframe(pompier.head())
    
def dataviz():
    st.write("### Datavisualisation")
    
    # Create a selectbox to choose between sections
    section_choice = st.selectbox("Choisir une section", ["Informations globales", "Délai d'intervention"])
    
    if section_choice == "Informations globales":
        accueil_dataviz()  # Function to display "Accueil Dataviz"
    elif section_choice == "Délai d'intervention":
        delai_intervention()  # Function to display "Délai d'intervention"

def accueil_dataviz():
    nbre_annees = pd.read_csv("Nombre_incident_annee.csv")
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=nbre_annees['CalYear'], y=nbre_annees['IncidentNumber'], line=dict(color='red')))
    fig1.update_layout(title="Graphique 1 - Nombre d'incidents par année", xaxis_title='Années', yaxis_title="Nombre d'incidents")
    st.plotly_chart(fig1)
    st.write("Le nombre d'incidents ne dépend pas de l'année")
    
    nbs = pd.read_csv("Nbs.csv")
    fig2 = go.Figure()
    fig2= px.line(nbs, x='Month', y='IncidentNumber', color='CalYear')
    fig2.update_layout(title="Graphique 2 - Nombre d'incidents par mois",xaxis_title='Mois',yaxis_title="Nombre d'incidents")
    st.plotly_chart(fig2)
    st.write("Le nombre d'incidents varie selon le mois")
    
    intervention_rate = pd.read_csv("intervention_rate.csv")
    fig3 = go.Figure(data=[go.Pie(labels=intervention_rate['IncidentGroup'], values=intervention_rate['IncidentNumber'])])
    fig3.update_layout(title="Graphique 3 - Taux d'intervention par groupe d'incidents")
    st.plotly_chart(fig3)
    
    if st.checkbox("Afficher la répartition des types d'interventions pour la catégorie SpecialService"):
        specialservice= pd.read_csv("specialservice.csv")
        fig4 = px.pie(specialservice, values='IncidentNumber', names='SpecialServiceType', title='Distribution des types d\'interventions pour SpecialService')
        st.plotly_chart(fig4)
    
    st.write("**Graphique 4 - Distribution de la variable distance**")
    st.image("./dist.png")
        

def delai_intervention():
    delai_seconds = 349
    delai_minutes = delai_seconds // 60
    delai_secondes_residuelles = delai_seconds % 60
    st.write("Le délai d'intervention moyen est de :", f"<span style='color: red;'>{delai_seconds} secondes</span> soit", f"<span style='color: red;'>{delai_minutes} min {delai_secondes_residuelles} secondes</span>", unsafe_allow_html=True)
    if st.checkbox("Distribution de la variable DelaiIntervention"):
        st.image("./distribution.png")
    
    pompier_group_year = pd.read_csv("pompier_group_year.csv")
    fig5 = go.Figure()
    fig5.add_trace(go.Scatter(x=pompier_group_year['CalYear'], y=pompier_group_year['DelaiIntervention'], line=dict(color='red')))
    fig5.update_layout(title="Graphique 1 - Délai d'intervention selon l'année", xaxis_title='Années', yaxis_title="Délai d'intervention moyen")
    st.plotly_chart(fig5)
    
    pompier_group_mois= pd.read_csv("pompier_group_mois.csv")
    fig6 = go.Figure()
    fig6.add_traces(go.Scatter(x= pompier_group_mois['Month'], y=pompier_group_mois['DelaiIntervention'], line=dict(color='red')))
    fig6.update_layout(title="Graphique 2 - Delai d'intervention selon le mois", xaxis_title='Mois', yaxis_title="Délai d'intervention moyen")
    st.plotly_chart(fig6)
    
    pompier_group_heures = pd.read_csv("pompier_group_heures.csv")
    fig7 = go.Figure()
    fig7.add_traces(go.Scatter(x= pompier_group_heures['HourOfCall'], y=pompier_group_heures['DelaiIntervention'], line=dict(color='red')))
    fig7.update_layout(title="Graphique 3 - Delai d'intervention selon l'heure", xaxis_title='Heures', yaxis_title="Délai d'intervention moyen")
    st.plotly_chart(fig7)
    
    st.write("Le délai d'intervention dépend du :", f"<span style='color: red;'>type d'incidents </span>. Le délai moyen est le plus long pour les feux, et le plus court pour les autres services ('Special Service') ", unsafe_allow_html=True)

    st.write("**Graphique 4 - Délai d'intervention en fonction de l'arrondissement**")
    st.image('./delai.png')

    st.write("**Graphique 5 - Délai d'intervention en fonction de la distance**")
    st.image("dist_delai.png")
    
def modelisation():
    st.write("### Modélisation")
    # Mettez ici votre code de modélisation
    st.write("Après le prétraitement de nos données, nous allons nous intéresser à la modélisation.")
    st.write("Deux approches sont étudiées.")
    
    section_choice = st.selectbox("Choix d'une approche",["Modélisation par Regression", "Modélisation par Classification"])
    
    if section_choice == "Modélisation par Regression":
        accueil_regression()  
    elif section_choice == "Modélisation par Classification":
        modelisation_regression()  

def accueil_regression():
    st.write("Avec la modélisation par régression, on inverse le problème.")
    st.write("On cherche à prédire le délai d'intervention.")
    st.markdown("<p style='color: red; font-weight: bold;'>Méthodologie</p>", unsafe_allow_html=True)
    st.write("La variable cible est contenue dans la colonne DelaiIntervention de notre Dataframe")
    st.write("Voici le dataframe de départ: ")
    regression= pd.read_csv("df5.csv")
    st.dataframe(regression.head())

    st.markdown("<p style='color: red; font-weight: bold;'>Modélisation</p>", unsafe_allow_html=True)
    st.write("Avant de lancer nos différents modèles, notre jeux de données a été séparé en deux jeux selon les proportions 80/20.")
    st.write("4  Modèles de regression sont testé. ")
    
    section_choice = st.selectbox("Choisir un modèle", ["LinearRegression","Arbre de décision", "RandomForest", "GradientBoostingRegressor"])

    if section_choice == "LinearRegression":
        st.image('linearregression.png')
    elif section_choice == "Arbre de décision":
        st.image('decisiontree.png')
    elif section_choice == "RandomForest":
        st.image("randomforest.png")
    elif section_choice == "GradientBoostingRegressor":
        st.image('gradienbosting.png')
        
    st.write("Le modèle de régression linéaire semble avoir des performances modérées, mais il pourrait bénéficier d'une amélioration. Le modèle de régression par arbre de décision a une performance élevée sur le jeu d'entraînement mais il souffre d'un overfitting sur le jeu de test, car le R² est considérablement plus bas sur ce dernier.Le modèle de régression par forêt aléatoire présente les mêmes conclusions. Le modèle de régression par Gradient Boosting semble avoir des performances relativement bonnes et cohérentes entre le jeu d'entraînement et le jeu de test mais méritent d'être amélioré.")
    
    st.write("La variable qui influence le plus le délai d'intervention est la **distance**.")
    
    st.markdown("<p style='color: red; font-weight: bold;'>Amélioration du modèle</p>", unsafe_allow_html=True)
    st.write("Afin d'améliorer le modèle, le modèle de régression par Gradient Boosting a été ajusté à l'aide de GridSearchCV.")
    st.write("Résultats obtenus : ")
    st.write("- Un coefficient de détermination  de 0.5147198858219273")    
    st.write("- MAE: 56.26258229196011")    
    st.write("- MSE: 5329.878653201203") 
    st.write("- RMSE: 73.00601792456018") 

    st.write(" MAE, MSE, RMSE sont des métriques qui quantifient les erreurs de prédiction d'un  modèle. Un MAE de 56.26 signifie que, en moyenne, les prédictions du modèle sont écartées d'environ 56.26 unités par rapport aux valeurs réelles.")
    st.write("Un MSE de 5329.87 indique que les erreurs individuelles sont en moyenne élevées et que le carré de ces erreurs est assez important.")
    st.write("Un RMSE de 73.006 est assez élevé, ce qui signifie que les erreurs de prédiction ont tendance à être relativement importantes.")

    st.write("**Conclusion:** On peut dire que ce modèle de régression présente des performances modérées. Le modèle capture une partie significative de la variance des données, mais il existe encore de l'erreur non capturée.")

def modelisation_classification():

    st.write("Nous allons nous intéresser à la modélisation par classification.")
    st.markdown("<p style='color: red; font-weight: bold;'>Méthodologie</p>", unsafe_allow_html=True)
    
    st.write("La variable cible est contenue dans la colonne distance de notre Dataframe")
    st.write("Afin de déterminer la distance, la valeur 1 représentera les distances inférieures à 2km, dites courtes et les distances longues prendront comme valeur 0")
    st.write("Voici le dataframe que l'on obtient: ")
    classification= pd.read_csv("df.csv")
    st.dataframe(classification.head())

    st.write("Avant de passer à la prédiction, il faut regarder si nos 2 classes sont également représentées ce qui est le cas ici.")
    st.image("classdistribution.png")

    st.markdown("<p style='color: red; font-weight: bold;'>Modélisation</p>", unsafe_allow_html=True)
    st.write("Avant de lancer nos différents modèles, notre jeux de données a été séparé en deux jeux selon les proportions 80/20.")
    st.write("3 Modèles de classification sont testé. ")

    section_choice = st.selectbox("Choisir un modèle", ["Arbre de décision", "RandomForest", "LogisticRegression"])

    if section_choice == "Arbre de décision":
        st.write('Accuracy: 0.78707192999543')
    elif section_choice == "RandomForest":
        st.write('Accuracy: 0.8519370378417256')
    elif section_choice == "LogisticRegression":
        st.write('Accuracy: Accuracy: 0.8044157420379541')
    
    st.write("Le meilleur modèle est le **RandomForest**")

    st.write("**La matrice de confusion**")
    st.image("matriceconfusion.png")
    st.write("**Le rapport de classification**")
    st.image("matriceclassification.png")
    st.write("**Importance feature**")
    st.image("featureimportance.png")    

    st.markdown("<p style='color: red; font-weight: bold;'>Amélioration du modèle</p>", unsafe_allow_html=True)
    st.write(" Pour essayer d'améliorer le modèle, nous ne gardons que les colonnes ayant le plus d'impact : DelaiIntervention, HourOfCall, Month, CalYear, IncidentGroup, PropertyCategory, IncidentStationGround et DeployedFromStation_Name.")
    st.write("Après application du modèle RandomForest, les résultats suivant sont obtenu :")
    st.write("**La matrice de confusion**")
    st.image("matriceconfusion2.png")
    st.write("**Le rapport de classification**")
    st.image("matriceclassification2.png")
    st.write("Globalement, ces mesures indiquent que le modèle a de bonnes performances pour les deux classes.")

def conclusion():
    st.write("Conlusion")   

    
    
pages = ["Accueil","Présentation du projet", "Exploration des données", "Datavisualisation", "Modélisation", "Conclusion"]

selected_page = st.sidebar.radio("Aller vers", pages)

# Gestion de la navigation
if selected_page == "Accueil":
    accueil()
elif selected_page == "Présentation du projet":
    presentation()
elif selected_page == "Exploration des données":
    jeudedonnee()
elif selected_page == "Datavisualisation":
    dataviz()
elif selected_page == "Modélisation":
    modelisation()
elif selected_page == "Prédiction":
    prediction()
elif selected_page == "Conclusion":
    conclusion()












