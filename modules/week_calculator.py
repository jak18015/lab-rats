import datetime

def get_week_number(date_str, date_format="%Y-%m-%d"):
    """
    Get the ISO week number for the given date string.

    Parameters:
    - date_str (str): A date string in the specified format.
    - date_format (str): The format of the input date string.

    Returns:
    - int: The ISO week number.
    """
    try:
        today = datetime.datetime.strptime(date_str, date_format).date()
        week_number = today.isocalendar()[1]
        return week_number
    except ValueError:
        print("Incorrect date format. Please use YYYY-MM-DD.")
        return None

def calculate_week_calculator(config):
    date_str = config.get("date_str", "2025-05-23")
    date_format = config.get("date_format", "%Y-%m-%d")

    return get_week_number(date_str, date_format)