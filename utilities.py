import requests, os
from termcolor import colored, cprint

# Getting user folder
user = os.getlogin()
key = 'sRkSnDSlvzNR4VVZpHh31vM83gNB1ndbeAANCoId'
file_length = []


def check_for_media_type(url_data):
    media_type = url_data["media_type"]

    if 'video' not in media_type:
        return True
    else:
        return False


def pic_downloader(user_url):
    file_request = requests.get('{}?api_key={}'.format(user_url, key))
    file_length.append(int(file_request.headers.get('content-length')))

    # Checking for the response status
    if file_request.status_code == 200:
        with open("C:/Users/{}/Downloads/image.jpg".format(user), 'wb') as file:
            file.write(file_request.content)


def checking_file_size():

    # Checking if file downloaded
    downloaded_length = os.path.getsize("C:/Users/{}/Downloads/image.jpg".format(user))
    if downloaded_length == file_length[0]:
        print(colored('The pic has been downloaded to your PC', 'blue'))
    else:
        print(colored('ERROR during download', 'red'))


def loading():
    loading1 = colored('Loading.', 'red', attrs=['reverse', 'blink'])
    loading2 = colored('.', 'red', attrs=['reverse', 'blink'])
    loading3 = colored('.', 'red', attrs=['reverse', 'blink'])
    loading4 = colored('.', 'red', attrs=['reverse', 'blink'])
    loading5 = colored('.', 'red', attrs=['reverse', 'blink'])

    loading_lst = [loading1, loading2, loading3, loading4, loading5]
    while True:

        for load in loading_lst:
            print(load, end='')
            time.sleep(1)
