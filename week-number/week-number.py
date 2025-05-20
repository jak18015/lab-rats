import datetime

def get_current_week_number():
    today = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    # ISO week number, Monday as the first day of the week
    week_number = today.isocalendar()[1]
    return week_number

if __name__ == "__main__":
    date_str = input("Enter a date (YYYY-MM-DD): ")
    # Validate the date format
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Incorrect date format. Please use YYYY-MM-DD.")
        exit(1)
    # Get the current week number
    week_number = get_current_week_number()
    print(f"Week number for {date_str}: {week_number}")