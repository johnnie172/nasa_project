import requests, json, os, sys, time
import user_input, utilities

user = os.getlogin()
key = 'sRkSnDSlvzNR4VVZpHh31vM83gNB1ndbeAANCoId'


def main():
    selected_date = user_input.get_date_from_user()

    response = requests.get('https://api.nasa.gov/planetary/apod?api_key={}&date={}'.format(key, selected_date))
    # checking for code 200 (ok)
    if response:
        print('**Success! we will now check the media type')
    else:
        print('An error has occurred.')
        print('Response cods: {}'.format(response))

#Getting the url dict:
    url_data = json.loads(response.text)

#Checking for media type:
    if utilities.check_for_media_type(url_data):
        selected_quality = user_input.get_quality_from_user(url_data)
        utilities.pic_downloader(selected_quality)
        utilities.checking_file_size()
    else:
        print("Sorry, we are currently not supporting video download, here is the link to the video:")
        print(url_data["url"])





if __name__ == '__main__':
    main()
