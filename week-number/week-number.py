import datetime

def get_current_week_number():
    today = datetime.date.today()
    # ISO week number, Monday as the first day of the week
    week_number = today.isocalendar()[1]
    return week_number

if __name__ == "__main__":
    print(f"Current week number: {get_current_week_number()}")