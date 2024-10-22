# Projet: Analyse du Temps de Réponse de la Brigade des Pompiers de Londres

## Contexte
Ce projet a été réalisé dans le but d'analyser les temps de réponse de la London Fire Brigade (Brigade des Pompiers de Londres), l'un des plus grands corps de pompiers au monde. L'objectif principal est de comprendre les facteurs influençant les délais d'intervention et de prédire le temps que les pompiers mettent pour arriver sur les lieux des incidents. Nous avons utilisé des données publiques sur les incidents de 2017 à 2022.

## Objectifs du projet
* Analyse exploratoire des données : Identifier les variables influentes.
* Prédiction des délais d'intervention : Modélisation par régression pour prédire le délai en secondes.
* Classification des délais d'intervention : Modélisation par classification pour catégoriser les délais (court ou long).

## Données
Les données proviennent de deux fichiers disponibles sur le site de la London Fire Brigade :

* Incident data : Données sur les incidents (incendies, fausses alertes, etc.).
* Mobilisation data : Informations sur le déploiement des unités de secours.
Les données contiennent plus de 940 000 incidents et sont décrites par 58 variables. Après un nettoyage et une fusion des données, nous avons conservé 44 variables pertinentes pour nos analyses.

Les deux fichiers sont disponibles sur le site: data.london.gov.uk

## Prétraitement des Données
  
* Suppression des colonnes inutiles : Colonnes redondantes ou contenant trop de valeurs manquantes.
* Gestion des valeurs manquantes : Remplacement des valeurs manquantes par la médiane pour les variables quantitatives et par des valeurs arbitraires pour certaines variables qualitatives.
* Standardisation des dates : Conversion des variables temporelles au format datetime.
* Ajout de nouvelles variables : Calcul de la distance entre la caserne et le lieu d'intervention grâce aux coordonnées géographiques.
 
## Modélisations

**1. Régression**

Nous avons testé plusieurs modèles de régression pour prédire les délais d'intervention, notamment :
* Régression linéaire
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor
  
**Modèle choisi :** Le Gradient Boosting Regressor a présenté les meilleurs résultats avec un score R² de 0.51.

**2. Classification**

Pour mieux comprendre les délais d'intervention, nous avons aussi développé un modèle de classification :
* Decision Tree Classifier
* Random Forest Classifier
* Logistic Regression
  
**Modèle choisi :** Le Random Forest Classifier s'est avéré le plus performant avec une AUC-ROC de 0.895 et une AUC-PR de 0.960, indiquant une bonne capacité à distinguer entre des délais courts et longs.

## Résultats
Les résultats montrent que la distance entre la caserne et le lieu de l'incident est la variable la plus influente dans la prédiction des délais d'intervention. Le modèle de régression et celui de classification offrent des perspectives intéressantes pour optimiser les interventions de la brigade.

## Difficultés et Limites
Volumétrie des données importante, nécessitant un prétraitement minutieux.
Performance limitée par la complexité des données géographiques et temporelles.
Manque d'intégration de certaines variables importantes comme les conditions de circulation.
Reproduction de l'Expérience

**Les notebooks utilisés dans ce projet sont disponibles dans ce dépôt :**
* Pompier.ipynb : Exploration des données.
* Modelisation_Regression.ipynb : Modélisation par régression.
* Modelisation_Classification.ipynb : Modélisation par classification.

## Futurs Développements
Nous pourrions améliorer ce projet en incluant des variables supplémentaires telles que :
* Temps passé sur le lieu de l’intervention.
* Conditions de circulation selon les jours et heures.


**Auteurs**
* Angeline Duqueyroix
* Aurélie Patron
* Soliman Traboulsi
