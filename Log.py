import logging

def setup_logging(log_file):
    """
    Configure logging to write to a log file.
    :param log_file: The path of the log file.
    """
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_message(message):
    """
    Record a message in the log file.
    :param message: The message to be recorded.
    """
    logging.info(message)
    print(message)

def log_error(error_message):
    """
    Record an error in the log file.
    :param error_message: The error message to be recorded.
    """
    logging.error(error_message)
    print(error_message)