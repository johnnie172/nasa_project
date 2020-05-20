import datetime


def get_date_from_user():
    user_input_date = \
        input('Would you like to get today pic or choose another date? (enter "today"/"another"): ').lower()

    if user_input_date[0] == 't':
        date = datetime.datetime.now().date()
    else:
        year = input('Enter a year(yyyy): ')
        month = input('Enter a month(mm): ')
        day = input('Enter a day(dd): ')
        date = '{}-{}-{}'.format(year, month, day)

    return date


def get_quality_from_user(url_data):
    user_input_hd = input('Do you want it in HD or not? (enter "HD"/"not"): ').lower()

    if user_input_hd[0] == "h":
        selected_quality_key = "hdurl"
    else:
        selected_quality_key = "url"

    return url_data[selected_quality_key]
