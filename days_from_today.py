from datetime import datetime

# Expects date in 'YYYY-MM-DD' format.
# Returns diff in days between date and today.
# In case of date in future, returns negative number.
def get_days_from_today(date: str) -> int:
    raw_date_pattern = "%Y-%m-%d"

    parsed_date = datetime.strptime(date, raw_date_pattern)

    today_date = datetime.today()

    # return days between two dates
    return today_date.toordinal() - parsed_date.toordinal()


def test_days_calculation():
    raw_input = input("Enter date in 'YYYY-MM-DD' format: ")
    try:
        days_between = get_days_from_today(raw_input)
        print(f"days between are {days_between}")
    except ValueError:
        print(f"Invalid input \'{raw_input}\'. Make sure you use 'YYYY-MM-DD' format")


test_days_calculation()