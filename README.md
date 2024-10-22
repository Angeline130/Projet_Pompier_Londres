# Projet: Analyse du Temps de Réponse de la Brigade des Pompiers de Londres

## Contexte
Ce projet a été réalisé dans le but d'analyser les temps de réponse de la London Fire Brigade (Brigade des Pompiers de Londres), l'un des plus grands corps de pompiers au monde. L'objectif principal est de comprendre les facteurs influençant les délais d'intervention et de prédire le temps que les pompiers mettent pour arriver sur les lieux des incidents. Nous avons utilisé des données publiques sur les incidents de 2017 à 2022.

## Objectifs du projet
*Analyse exploratoire des données : Identifier les variables influentes.
*Prédiction des délais d'intervention : Modélisation par régression pour prédire le délai en secondes.
*Classification des délais d'intervention : Modélisation par classification pour catégoriser les délais (court ou long).

## Jeux de Données:
- fichier https://data.london.gov.uk/dataset/london-fire-brigade-incident-records 
- fichier https://data.london.gov.uk/dataset/london-fire-brigade-mobilisation-records

Les deux fichiers sont disponibles sur le site: data.london.gov.uk

## Analyse des jeux de données
##### - London-fire-brigade-incident-records
###### DataFrame de 21 colonnes et de ..........lignes.
##### Les variables sont:
* IncidentNumber: Numéro d'incident
* DateOfCall: Date de l'appel
* CalYear: Année de l'appel
* TimeOfCall: Heure complete a laquelle l'appel est passé
* HourOfCall: Heure de l'appel uniquement
* IncidentGroup: Catégorie de l'incident
* StopCodeDescription: Détail de la Catégorie d'incident
* SpecialServiceType: description pour la catégorie SpecialService
* PropertyCategory: Description de la propriété 1er niveau
* PropertyType: Description de la propriété
* AdressQualifier: Descrit la localisation actual de l'incident selon la categorie précédente
* Postcode_full: code postal entier
* Postcode_district: code postal du district
* UPRN
* USRN
* IncGeo_BoroughCode: Numéro de l'arrondissement
* IncGeo_BoroughName: Nom de l'arrondissement
* ProperCase: Nom de l'arrondissement
* IncGeo_WardCode: Code du quartier
* IncGeo_WardName : Nom du quartier
* IncGeo_WardNameNew: Nouveau nom de quartier
* Easting_m:  Coordonnées cartésiennes Est
* Northing_m:  Coordonnées cartésiennes Nord
* Easting_rounded:  Coordonnées cartésiennes Est arrondies
* Northing_rounded:  Coordonnées cartésiennes Nord arrondies
* Latitude
* Longitude
* FRS: Terrain des pompier
* IncidentStationGround: Station dans le secteur
* FirstPumpArriving_AttendanceTime : Temps de présence de la première pompe en secondes
* FirstPumpArriving_DeployedFromStation: Nom de la station qui envoie le premier camion
* SecondPumpArriving_AttendanceTime Temps de présence de la deuxieme pompe en secondes
* SecondPumpArriving_DeployedFromStation: Nom de la station qui envoie le second camion
* NumStationsWithPumpsAttending: Nombre de stations ayant un camion en action
* NumPumpsAttending: Nombre de camions en intervention
* PumpCount: Nombre de camions
* PumpMinutesRounded: Temps passé par les camions lors d'un incident, arrondi à l'heure la plus proche
* Notional Cost (£): Coût
* NumCalls: Nombre d'appel


##### - London-fire-brigade-mobilisation-records
###### DataFrame de 21 colonnes et de ..............lignes.**
##### Les variables sont:
* IncidentNumber: Numéro d'incident
* CalYear : Année de l'appel
* HourOfCall: Heure de l'appel
* ResourceMobilisationId: Id de la source mobilisée
* Resource_Code: Code de la ressource
* PerformanceReporting: Premier camion arrivé au niveau de l'incident
* DateAndTimeMobilised: Date et Heure à laquelle le message arrive à la caserne
* DateAndTimeMobile: Date et heure à laquelle ils partent de la caserne
* DateAndTimeArrived: Date et Heure à laquelle ils arrivent au niveau de l'incident
* TurnoutTimeSeconds: Temps entre l'appel et le départ des pompiers
* TravelTimeSeconds: Temps de trajet en secondes
* AttendanceTimeSeconds: Temps d'intervention en secondes
* DateAndTimeLeft: Date et heure de départ du lieu de l'accident
* DateAndTimeReturned: Date et heure de retour à la caserne
* DeployedFromStation_Code: Code de la station déployée
* DeployedFromStation_Name: Nom de la station déployée
* DeployedFromLocation: Lieu d'ou part le camion
* PumpOrder: Nombre de véhicules
* PlusCode_Code
* PlusCode_Description: Description du PlusCode
* DelayCodeId: Code correspondant à un type de retard
* DelayCode_Description: Raisons du retard


  ## Fusion des deux Dataframes
  ## Analyse de nos données
  ## Visualisation
  ## Modélisation  
