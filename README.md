# API_Tide_SHOM - SHOM Tide Data Retrieval Application
The application retrieves marigraphic data through the SHOM API based on configuration parameters specified in a JSON configuration file.

## Description:
This repository contains an application designed to retrieve tide data from the French Navy Hydrographic and Oceanographic Service (SHOM) using its API (https://services.data.shom.fr/). The SHOM collects and manages information about seas and oceans, producing underwater maps, measuring tides and currents, and providing crucial data for maritime navigation, safety at sea, and oceanographic research. In essence, SHOM helps understand and navigate marine environments.

The application retrieves marigraphic data through the SHOM API based on configuration parameters specified in a JSON configuration file.

## Features:

- Retrieval of tide data from the SHOM API.
- Configuration of acquisition parameters via a JSON configuration file.
- Generation of API requests to retrieve data.
- Creation of data files from the obtained results.

## Code Structure:

The code is divided into several modules to enhance readability and maintenance. Here's a brief overview of each module:

- API_Management.py: Contains functions to query and retrieve data from the API.
- Log.py: Manages logging configuration to record messages and errors in a log file.
- Configuration_Import.py: Handles the import of configuration parameters from a JSON file.
- API_Request_Creation.py: Contains functions to generate API requests based on parameters.
- Data_File_Writing.py: Contains functions to create data files from results.
- API_Tide_SHOM.py: Entry point of the application, orchestrates the data retrieval and processing steps.

## Usage:

1. Clone this repository to your local machine.
2. Configure acquisition parameters in the Configuration.json file and update 'config_file_path' in the API_Tide_SHOM.py script with a valid path.
3. Update 'log_file' in the API_Tide_SHOM.py script with a valid path.
4. Execute the API_Tide_SHOM.py script to initiate the processing.
5. Retrieved data will be saved in the directory specified in the configuration file.

## Execution Time Measurement:

The execution time of the application can be measured using Python's time module.

## Contributions:

Contributions are welcome! If you'd like to make improvements or fix issues, feel free to create a pull request.

## Disclaimer:

Please note that the use of this application is subject to the terms of use of https://services.data.shom.fr/. Ensure compliance with the usage rules before running the processing.

_________________________________________________________________________________________________________________________________________________________________________________________________________________________

# API_Tide_SHOM Application de Récupération de Données des Marées SHOM

## Description:

Ce dépôt contient une application conçue pour récupérer des données de marées auprès du Service Hydrographique et Océanographique de la Marine (SHOM) en utilisant son API (https://services.data.shom.fr/). Le SHOM collecte et gère des informations sur les mers et les océans, produit des cartes sous-marines, mesure les marées et les courants, et fournit des données essentielles pour la navigation maritime, la sécurité en mer et la recherche océanographique. En essence, le SHOM aide à comprendre et à naviguer dans les environnements marins.

L'application récupère des données marégraphiques via l'API SHOM en fonction de paramètres de configuration spécifiés dans un fichier de configuration JSON.

## Fonctionnalités:

- Récupération de données de marées depuis l'API SHOM.
- Configuration des paramètres d'acquisition via un fichier de configuration JSON.
- Génération de requêtes API pour récupérer les données.
- Création de fichiers de données à partir des résultats obtenus.

## Structure du Code:

Le code est divisé en plusieurs modules pour améliorer la lisibilité et la maintenance. Voici un aperçu de chaque module :

- API_Management.py: Contient des fonctions pour interroger et récupérer des données depuis l'API.
- Log.py: Gère la configuration du journal pour enregistrer les messages et erreurs dans un fichier de log.
- Configuration_Import.py: Gère l'importation des paramètres de configuration depuis un fichier JSON.
- API_Request_Creation.py: Contient des fonctions pour générer des requêtes API en fonction des paramètres.
- Data_File_Writing.py: Contient des fonctions pour créer des fichiers de données à partir des résultats.
- API_Tide_SHOM.py: Point d'entrée de l'application, orchestre les étapes de récupération et de traitement des données.

## Utilisation:

1. Clonez ce dépôt sur votre machine locale.
2. Configurez les paramètres d'acquisition dans le fichier Configuration.json et mettez à jour 'config_file_path' dans le script API_Tide_SHOM.py avec un chemin valide.
3. Mettez à jour 'log_file' dans le script API_Tide_SHOM.py avec un chemin valide.
4. Exécutez le script API_Tide_SHOM.py pour lancer le traitement.
5. Les données récupérées seront enregistrées dans le répertoire spécifié dans le fichier de configuration.

## Mesure du Temps d'Exécution:

Le temps d'exécution de l'application peut être mesuré en utilisant le module time de Python.

## Contributions:

Les contributions sont les bienvenues ! Si vous souhaitez apporter des améliorations ou corriger des problèmes, n'hésitez pas à créer une demande de pull.

## Avertissement:

Veuillez noter que l'utilisation de cette application est soumise aux conditions d'utilisation de https://services.data.shom.fr/. Assurez-vous de respecter les règles d'utilisation avant de lancer le traitement.
