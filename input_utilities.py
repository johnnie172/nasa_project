import datetime


# Asking the user to choose a date:
def get_date_from_user():
    user_input_date = \
        input('Would you like to get today pic or choose another date? (enter "today"/"another"): ').lower()

    if user_input_date[0] == 't':
        date = datetime.datetime.now().date()
        return date
    else:
        return get_another_date_from_user()


def get_another_date_from_user():
    year = input('Enter a year(yyyy): ')
    month = input('Enter a month(mm): ')
    day = input('Enter a day(dd): ')
    date = '{}-{}-{}'.format(year, month, day)
    return date



# Asking the user for hd or not pic:
def get_quality_from_user(url_data):
    user_input_hd = input('Do you want it in HD or not? (enter "HD"/"not"): ').lower()
    selected_quality_key = "hdurl" if user_input_hd[0] == "h" else "url"

    return url_data[selected_quality_key]
