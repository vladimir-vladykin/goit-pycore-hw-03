from datetime import datetime, date, timedelta

name_key = "name"
birthday_key = "birthday"
congratulation_date_key = "congratulation_date"
date_pattern = "%Y.%m.%d"
days_of_upcoming_range = 7
iso_saturday = 6
iso_sunday = 7

# expects list of users with name and birthday in 'YYYY.MM.DD'
def get_upcoming_birthdays(users: list):
    current_date = datetime.today().date()
    current_year = current_date.year

    # result is gonna be list with dicts, each with fields like "name" and "congratulation_date"
    upcoming_birthdays_result = []

    # iterate throudg users to find out who has upcoming birthday
    for user in users:
        # parse user's birthdate
        birthday_date = datetime.strptime(user[birthday_key], date_pattern).date()
        
        # figure out date of celebration this year 
        birthday_month = birthday_date.month
        birthday_day = birthday_date.day    
        this_year_birthday_date = date(current_year, birthday_month, birthday_day)
        
        is_birthday_passed = this_year_birthday_date < current_date

        congrats_date: date
        if is_birthday_passed:
            # we will check for date in next year
            congrats_date = date(current_year + 1, birthday_month, birthday_day)
        else:
            congrats_date = this_year_birthday_date

        
        # we have to move congrats date if it's on weekend
        congrats_day_of_week = congrats_date.isoweekday()
        is_congrats_date_in_weekend = congrats_day_of_week >= iso_saturday
        if is_congrats_date_in_weekend:
            # we will add one day is this is Sunday, and two if this is Saturday
            days_factor = 1 if congrats_day_of_week == iso_sunday else 2
            congrats_date = congrats_date + timedelta(days=days_factor)


        
        # we now have final congrats date, now let's figure out should we 
        # include it in upcoming list

        if (congrats_date.toordinal() - current_date.toordinal()) <= days_of_upcoming_range:
            upcoming_birthdays_result.append(
                {
                    name_key: user[name_key], 
                    congratulation_date_key: datetime.strftime(congrats_date, date_pattern)
                }
            )
        # otherwise congrats date is not soon enough, so we do not consider it's as upcoming for now


    return upcoming_birthdays_result

def test_bitrhdays():
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
        {"name": "Jake Doe", "birthday": "1994.07.19"},
        {"name": "Jane Doe", "birthday": "1990.07.10"},
        {"name": "John Smith", "birthday": "1990.07.6"},
        {"name": "Agent Smith", "birthday": "1990.07.07"}
    ]
    print("We're testing this list of users:\n", users)

    upcoming_birthdays = get_upcoming_birthdays(users)
    print("List of upcoming congratulations:\n", upcoming_birthdays)




test_bitrhdays()
