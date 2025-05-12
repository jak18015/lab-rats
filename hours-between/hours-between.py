from datetime import datetime

def hours_between_dates(date1_str, date2_str, date_format="%Y-%m-%d %H:%M"):
    """
    Calculates the number of hours between two dates given in 'YYYY-MM-DD HH:MM' format.

    Parameters:
    - date1 (str): The first date as a string.
    - date2 (str): The second date as a string.
    - date_format (str): The format of the input date strings. Default is 'YYYY-MM-DD HH:MM'.

    Returns:
    - float: The number of hours between the two dates.
    """
    try:
        date1 = datetime.strptime(date1_str, date_format)
        date2 = datetime.strptime(date2_str, date_format)
        delta = abs(date2 - date1)
        return delta.total_seconds() / 3600
    except ValueError as e:
        print(f"Error parsing dates: {e}")
        return None

date1 = "2025-05-11 13:00"
date2 = "2025-05-12 10:30"
print(f"\ninfection timepoint: {date1}")
print(f"timepoint1: {date1}\n\t{hours_between_dates(date1, date2)} hpi")

date2 = "2025-05-12 16:30"
print(f"timepoint2: {date2}\n\t{hours_between_dates(date1, date2)} hpi")
