import requests
from Log import log_message, log_error

# List of functions to query and retrieve data from the API

def func_api_request(url_API):
    """
    Retrieve data from the web API
    :param url_API: URL of the API page
    :return: Returns the API data or raises an error if the URL is incorrect.
    """
    try:
        # Retrieve the status of the web API
        response = requests.get(url_API)
        response.raise_for_status()  # Check if the response is successful (200 OK)
    except requests.exceptions.RequestException as e:
        # In case of request error (e.g., incorrect URL)
        message_log = f"Error in API request: {e}"
        log_error(message_log)
        raise

    # If the request succeeded (status 200 OK)
    message_log = f"Connection to the API successful. Starting data retrieval."
    log_message(message_log)

    # Retrieve JSON data from the response
    data = response.json()['data']

    # Constructing data
    line = "DateTime;Water Level\n\r\r"

    for raw in data:
        date_raw = raw['timestamp']
        date = date_raw.replace("/", "-")
        measurement = str(raw['value'])
        line += f"{date};{measurement}\n"

    message_log = f"Data retrieval completed."
    log_message(message_log)

    # Return the API data
    return line