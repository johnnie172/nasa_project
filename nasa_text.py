import requests, json, os, sys, time
import user_input, utilities
from termcolor import colored, cprint

user = os.getlogin()
key = 'sRkSnDSlvzNR4VVZpHh31vM83gNB1ndbeAANCoId'
downloaded = colored('\nYou got the image', 'green')


def main():
    selected_date = user_input.get_date_from_user()

    response = requests.get('https://api.nasa.gov/planetary/apod?api_key={}&date={}'.format(key, selected_date))

    # checking for code 200 (ok)
    if response:
        print('**Success!! you will soon get the pic!')
    else:
        print('An error has occurred.')
        print('Response cods: {}'.format(response))

#Getting the url text
    response_dict = json.loads(response.text)

    selected_quality = user_input.get_quality_from_user(response_dict)

    utilities.file_downloader(selected_quality)




if __name__ == '__main__':
    main()
