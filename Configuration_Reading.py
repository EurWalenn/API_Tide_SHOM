import json

def func_import_config_file(config_file_path, element_to_load):
    """
    Function to manage the configuration file and load information
    :param config_file_path: Path of the configuration file
    :param element_to_load: Elements to retrieve from the configuration file
    :return: List of elements necessary for application management
    """
    try:
        with open(config_file_path, 'r') as f:
            config_data = json.load(f)[element_to_load]
        message = f"The file {config_file_path} has been found."
        return config_data
    except FileNotFoundError:
        message = f"The file {config_file_path} was not found."
        raise Exception(message)
    except KeyError:
        message = f"The section {element_to_load} was not found in the file {config_file_path}."
        raise Exception(message)
    except json.JSONDecodeError:
        message = f"Error while reading JSON file {config_file_path}."
        raise Exception(message)
