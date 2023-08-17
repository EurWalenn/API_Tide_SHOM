from Log import log_message, log_error

def func_create_data_file(File_Path, Data):
    """
    Function to create a data file after connecting to the API to retrieve SHOM data
    :param File_Path: Location to copy the data file
    :param Data: Data to be included in the data file
    :return: None (no explicit return value)
    """
    try:
        message_log = f"Creating data file."
        log_message(message_log)

        # Open the file in write mode ("w")
        with open(File_Path, "w") as File:
            message_log = f"Writing to the data file"
            log_message(message_log)

            # Write data to the file
            File.write(Data)

        message_log = f"Writing completed. Closing the data file."
        log_message(message_log)

    except Exception as e:
        # In case of error during file creation or writing
        message_log = f"Error in file creation/writing: {e}"
        log_error(message_log)
        raise