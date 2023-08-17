#!/usr/bin/env python3

import time
from API_Management import func_api_request
from Log import setup_logging, log_message
from Configuration_Import import func_retrieve_configuration
from API_Request_Creation import func_date_query_management
from Data_File_Writing import func_create_data_file
import os

# Configuration file
config_file_path = "//Configuration.json"

# Create log file
log_file = '//Log/Fichier_Log_API_SHOM.txt'
setup_logging(log_file)

# Launch the application
message_log = f"----------------------------------------------------"
log_message(message_log)

message_log = 'Processing started...'
log_message(message_log)

start_time = time.time()

# Import configuration
message_log = 'Starting retrieval of variables from the configuration file.'
log_message(message_log)

config_values = func_retrieve_configuration(config_file_path)

message_log = 'Finished retrieving variables from the configuration file.'
log_message(message_log)

# Loop to retrieve configuration information + file-by-file processing
for Acquisition_Line_Name, Data_Format, SHOM_ID, Data_Sources, Measurement_Interval, File_Name, Export_Directory, Backup_Day, \
        in config_values:
    message_log = f"+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+"
    log_message(message_log)

    message_log = f"Starting processing of Acquisition Line {Acquisition_Line_Name}."
    log_message(message_log)

    # Retrieve dates for API request creation
    message_log = f"Retrieving start and end dates for the request of file " \
                  f"{Acquisition_Line_Name}."
    log_message(message_log)

    Start_Date, End_Date = func_date_query_management(Backup_Day)

    # Create API request
    API_Link = f"https://services.data.shom.fr/maregraphie/observation/{Data_Format}/{SHOM_ID}?sources={Data_Sources}" \
               f"&dtStart={Start_Date}&dtEnd={End_Date}&interval={Measurement_Interval}"

    message_log = f"Creating API request: {API_Link}."
    log_message(message_log)

    # Retrieve data from API
    message_log = f"Retrieving data from the API"
    log_message(message_log)

    API_Data = func_api_request(API_Link)

    # Create data file
    File_Path = os.path.join(Export_Directory, File_Name)

    message_log = f"Starting creation of data file '{File_Path}'."
    log_message(message_log)

    func_create_data_file(File_Path, API_Data)

    message_log = f"Data file '{File_Path}' has been created."
    log_message(message_log)

    message_log = f"Finished processing of Acquisition Line {Acquisition_Line_Name}."
    log_message(message_log)

end_time = time.time()
execution_time = end_time - start_time

message_log = f"Application processing completed in {execution_time} secondes"
log_message(message_log)