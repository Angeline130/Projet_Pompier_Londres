# Projet_Pompier_Londres

## Objectif du travail: 
Réussir à prédire le temps de Réponse de la Brigade des Pompiers de Londres

## Jeux de Données:
- fichier https://data.london.gov.uk/dataset/london-fire-brigade-incident-records 
- fichier https://data.london.gov.uk/dataset/london-fire-brigade-mobilisation-records

Les deux fichiers sont disponibles sur le site: data.london.gov.uk

## Analyse des jeux de données
- London-fire-brigade-incident-records
DataFrame de 21 colonnes et de ..........lignes.
Colonnes: IncidentNumber
DateOfCall
CalYear
TimeOfCall
HourOfCall
IncidentGroup
StopCodeDescription
SpecialServiceType
PropertyCategory
PropertyType	
FirstPumpArriving_AttendanceTime
FirstPumpArriving_DeployedFromStation
SecondPumpArriving_AttendanceTime
SecondPumpArriving_DeployedFromStation
NumStationsWithPumpsAttending
NumPumpsAttending	PumpCount
PumpMinutesRounded
Notional Cost (£)
NumCalls


- London-fire-brigade-mobilisation-records
DataFrame de 21 colonnes et de ..............lignes.
*Colonnes: IncidentNumber": "Numéro d'incident
         * CalYear : Année de l'appel
         * HourOfCall: Heure de l'appel
         * ResourceMobilisationId: 
         * Resource_Code
          PerformanceReporting
          DateAndTimeMobilised: Date et Heure à laquelle le message arrive à la caserne
          DateAndTimeMobile: Date et heure à laquelle ils partent de la caserne
          DateAndTimeArrived: Date et Heure à laquelle ils arrivent au niveau de l'incident
          TurnoutTimeSeconds: Temps entre l'appel et le départ des pompiers
          TravelTimeSeconds: Temps de trajet en secondes
          AttendanceTimeSeconds: Temps d'intervention en secondes
          DateAndTimeLeft: Date et heure de départ du lieu de l'accident
          DateAndTimeReturned: Date et heure de retour à la caserne
          DeployedFromStation_Code: Code de la station déployée
          DeployedFromStation_Name: Nom de la station déployée
          DeployedFromLocation: Lieu d'ou part le camion
          PumpOrder: Nombre de véhicules
          PlusCode_Code: 
          PlusCode_Description
          DelayCodeId: Code correspondant à un type de retard
          DelayCode_Description: Raisons du retard

  ## Fusion des deux Dataframes 
