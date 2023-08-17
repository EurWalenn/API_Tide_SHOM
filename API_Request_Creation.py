from datetime import datetime
from datetime import timedelta
from Log import log_message, log_error

def func_date_query_management(Days_Backward):
    """
    Function to generate start and end dates for a query
    :param Days_Backward: Number of days to go back (maximum of 31 days - Limitation from this API)
    :return: Start_Query_Date, End_Query_Date
    """
    try:
        message_log = "Retrieving current date"
        log_message(message_log)

        now = datetime.now()  # current date and time

        if int(Days_Backward) > 31:
            message_log = f"Number of days backward is greater than 31 days: {Days_Backward}. " \
                          f"The value is therefore set to 31 days."
            log_message(message_log)
            Days_Backward = "30"
        else:
            message_log = f"Number of days backward is less than 31 days: {Days_Backward}. " \
                           f"The value remains unchanged."
            log_message(message_log)

        # Start date for the query
        Before_Date = now - timedelta(days=int(Days_Backward))
        year_before = Before_Date.strftime("%Y")
        month_before = Before_Date.strftime("%m")
        day_before = Before_Date.strftime("%d")
        hour_before = Before_Date.strftime("%H")
        Start_Query_Date = year_before + "-" + month_before + "-" + day_before + "T" + hour_before + "%3A00%3A00Z"

        message_log = f"Retrieving start date for the query: {Start_Query_Date}."
        log_message(message_log)

        # End date for the query
        Current_Date = now
        year = Current_Date.strftime("%Y")
        month = Current_Date.strftime("%m")
        day = Current_Date.strftime("%d")
        hour = Current_Date.strftime("%H")
        End_Query_Date = year + "-" + month + "-" + day + "T" + hour + "%3A00%3A00Z"

        message_log = f"Retrieving end date for the query: {End_Query_Date}."
        log_message(message_log)

        return Start_Query_Date, End_Query_Date
    except Exception as e:
        # In case of error in date management
        message_log = f"Error in date management: {e}"
        log_error(message_log)
        raise