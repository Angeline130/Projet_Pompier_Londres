🚒 Analyse des temps de réponse – London Fire Brigade (2017–2022)

🎯 Objectif

Analyser les facteurs influençant les délais d’intervention des pompiers et identifier des leviers d’optimisation opérationnelle.

🛠️ Stack technique

Python (Pandas, Scikit-learn)

Data visualisation (Matplotlib, Seaborn)

Machine Learning (régression, classification)

📊 Données

Source : London Fire Brigade (data.london.gov.uk)

~940 000 incidents analysés

44 variables après nettoyage et préparation

🔍 Réalisations

Nettoyage, fusion et préparation de données multi-sources

Feature engineering :
- création de variables temporelles
- calcul de la distance caserne → intervention
- 
Analyse exploratoire pour identifier les variables clés

Modélisation :
- régression pour prédire le temps d’intervention
- classification pour distinguer délais courts / longs

📈 Résultats

La distance est le facteur le plus déterminant dans les délais d’intervention
Modèle de classification performant (AUC ~0.90)

Identification de variables clés influençant la rapidité d’intervention

💡 Apports métier

Mise en évidence de leviers d’optimisation des temps d’intervention

Possibilité d’améliorer l’allocation des ressources

Aide à la prise de décision opérationnelle

⚠️ Limites

Absence de données trafic (impact potentiel majeur)

Complexité des variables géographiques

Données partiellement incomplètes

👉 Notebooks disponibles (EDA, régression, classification)

**Auteurs**
* Angeline Duqueyroix
* Aurélie Patron
* Soliman Traboulsi
