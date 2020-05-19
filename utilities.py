import requests, os

#Getting user folder
user = os.getlogin()
key = 'sRkSnDSlvzNR4VVZpHh31vM83gNB1ndbeAANCoId'

def file_downloader(user_url):
    file_request = requests.get('{}?api_key={}'.format(user_url, key))
    file_length = int(file_request.headers.get('content-length'))

    #Checking for the response status
    if file_request.status_code == 200:
        with open("C:/Users/{}/Downloads/image.jpg".format(user), 'wb') as file:
            file.write(file_request.content)

    downloaded_length = os.path.getsize("C:/Users/{}/Downloads/image.jpg".format(user))

    # Checking if file downloaded
    if downloaded_length == file_length:
        print("The pic has been downloaded to your PC")
    else:
        print("ERROR during download")


def loading():
    loading1 = colored('Loading.', 'red', attrs=['reverse', 'blink'])
    loading2 = colored('.', 'red', attrs=['reverse', 'blink'])
    loading3 = colored('.', 'red', attrs=['reverse', 'blink'])
    loading4 = colored('.', 'red', attrs=['reverse', 'blink'])
    loading5 = colored('.', 'red', attrs=['reverse', 'blink'])

    loading_lst = [loading1, loading2, loading3, loading4, loading5]
    for load in loading_lst[0:4]:
        print(load, end='')
        time.sleep(1)