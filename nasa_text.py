
import requests
import datetime
import json

date = datetime.datetime.now().date()
key = 'sRkSnDSlvzNR4VVZpHh31vM83gNB1ndbeAANCoId'

def user_date():
    year = int(input('Enter a year(yyyy): '))
    month = int(input('Enter a month(mm): '))
    day = int(input('Enter a day(dd): '))
    date = str(year)+"-"+str(month)+"-"+str(day)
    return date

def choose_q(user_url):

    print('Please wait..')

    Picture_request = requests.get('{}?api_key={}'.format(user_url, key))
    if Picture_request.status_code == 200:
        with open("C:/Users/jmpst/Downloads/image.jpg", 'wb') as f:
            f.write(Picture_request.content)

            print("You got the image!")

user_input_date = input('Would you like to get today pic or choose another date? (enter "today"/"another"): ').lower()


if user_input_date[0] == 't':
    date = date
else:
    user_date()


response = requests.get('https://api.nasa.gov/planetary/apod?api_key={}&date={}'.format(key, date))
response_dict = json.loads(response.text)

hd_url = response_dict["hdurl"]
pic_url = response_dict["url"]


if response:
    print('**Success!! you will soon get the pic!')
else:
    print('An error has occurred.')
    print('Response cods: {}'.format(response))


user_input_hd = input('Do you want it in HD or not? (enter "HD"/"not"): ').lower()


if user_input_hd[0] == "h":
      choose_q(hd_url)
else:
    choose_q(pic_url)
