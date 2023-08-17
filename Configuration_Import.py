from Configuration_Reading import func_import_config_file
from Log import log_message, log_error

def func_retrieve_configuration(config_file_path):
    """
    Retrieve elements from the configuration file
    :return: List of elements from the configuration file
    """
    try:
        message_log = "Retrieving content from the configuration file."
        log_message(message_log)

        try:
            Config = func_import_config_file(config_file_path,element_to_load="Configuration")
            log_message(f"The file {config_file_path} has been found and loaded successfully.")
        except Exception as e:
            message_log = f"Error during configuration file loading: {e}"
            log_error(message_log)
            raise

        message_log = "Sorting elements from the configuration file."
        log_message(message_log)

        value_list = []  # Create a list to store the values

        for config_item in Config:
            Acquisition_Line_Name = config_item['Acquisition_Line_Name']
            Data_Format = config_item['Data_Format']
            SHOM_ID = config_item["SHOM_ID"]
            Sources = config_item["Sources"]
            Measurement_Interval = config_item["Measurement_Interval"]
            File_Name = config_item['File_Name']
            Export_Directory = config_item['Export_Directory']
            Backup_Day = config_item['Backup_Day']

            if not all([Acquisition_Line_Name, Data_Format, SHOM_ID, Sources, Measurement_Interval, File_Name,
                        Export_Directory, Backup_Day]):
                message = f"Missing data in the configuration: {config_item}"
                raise Exception(message)

            # Add the values to the list
            value_list.append((Acquisition_Line_Name, Data_Format, SHOM_ID, Sources, Measurement_Interval, File_Name,
                                  Export_Directory, Backup_Day))

        # Return the complete list containing all values
        return value_list

    except Exception as e:
        message_log = f"Error during configuration retrieval: {e}"
        log_error(message_log)
        raise