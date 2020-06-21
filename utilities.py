import requests, os, re, time
from termcolor import colored
from pathlib import Path
import consts
from consts import KEY

get_user_home_path = str(Path.home())
file_length = []


# Chacking if there is pic or video in the specific date:
def check_for_media_type(url_data):
    media_type = url_data[consts.MEDIA_TYPE]

    return consts.VIDEO not in media_type


# Downloading the pic:
def pic_downloader(user_url):
    file_request = requests.get('{}?api_key={}'.format(user_url, KEY))
    file_length.append(int(file_request.headers.get('content-length')))

    # Checking for the response status:
    if file_request.status_code == 200:
        with open('{}/image.jpg'.format(get_user_home_path), 'wb') as file:
            file.write(file_request.content)
            return False


# Making a description file:
def make_explanation_text_file(url_data):
    # Getting the text:
    text = str(url_data["explanation"])
    # Making the text readable and not one liner:
    splitted_text = re.findall(r'(?:\d[,.]|[^,.])*(?:[,.]|$)', text)
    # Deleting the spaces in the beginning of each line:
    new_splitted_text = [line[1:] for line in splitted_text[1:]]
    new_splitted_text = [splitted_text[0]] + new_splitted_text
    splitted_text = "\n".join(new_splitted_text)
    # Opening the file and writing the text:
    with open('{}/image_explanation.txt'.format(get_user_home_path), 'w') as text_file:
        text_file.write(splitted_text)


# Checking if file downloaded:
def checking_file_size():
    downloaded_length = os.path.getsize('{}/image.jpg'.format(get_user_home_path))
    if downloaded_length == file_length[0]:
        print(colored('\nThe pic and explanation txt file has been downloaded to your PC at directory: {}'.format(
            get_user_home_path),
            'blue'))
    else:
        print(colored('ERROR during download', 'red'))
