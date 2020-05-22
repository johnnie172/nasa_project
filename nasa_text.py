import requests, json, os, sys, time
import user_input, utilities


def main():
    selected_date = user_input.get_date_from_user()

    response = requests.get(
        'https://api.nasa.gov/planetary/apod?api_key={}&date={}'.format(utilities.key, selected_date))
    # checking for code 200 (ok):
    if response:
        print('**Success! we will now check the media type')
        # Getting the url dict:
        url_data = json.loads(response.text)
        # Checking for media type:
        if utilities.check_for_media_type(url_data):
            # Making text file with pic explanation:
            utilities.make_text_file(url_data)
            # Asking for quality to download
            selected_quality = user_input.get_quality_from_user(url_data)
            # Downloading the pic:
            utilities.pic_downloader(selected_quality)
            # Making sure the file downloaded correctly:
            utilities.checking_file_size()
        else:
            print("Sorry, we are currently not supporting video download, here is the link to the video:")
            print(url_data["url"])
    else:
        print('An error has occurred.')
        print('Response cods: {}'.format(response))


if __name__ == '__main__':
    main()
