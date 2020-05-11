import requests
import datetime
import json

user_input_date = input('Would you like to get today pic or choose another date? (enter today/another): ').lower()
if user_input_date[0] == 't':
    date = datetime.datetime.now().date()
else:
    year = int(input('Enter a year(yyyy):'))
    month = int(input('Enter a month(mm):'))
    day = int(input('Enter a day(dd):'))
    date = str(year)+"-"+str(month)+"-"+str(day)

key = 'sRkSnDSlvzNR4VVZpHh31vM83gNB1ndbeAANCoId'



response = requests.get('https://api.nasa.gov/planetary/apod?api_key={}&date={}'.format(key, date))

if response:
    print('**Success!! you will soon get the pic!')
else:
    print('An error has occurred.')
    print('Response cods: {}'.format(response))


response_dict = json.loads(response.text)
hd_url = response_dict["hdurl"]
pic_url = response_dict["url"]


# user_input = input("Would you like to get the pic? ").lower()
# if user_input[0] == 'y':
user_input_hd = input("""Do you want it in HD or not? (enter "HD"/"not"): """).lower()
if user_input_hd[0] == "h":
    print('Please wait..')
    Picture_request = requests.get('{}?api_key=sRkSnDSlvzNR4VVZpHh31vM83gNB1ndbeAANCoId'.format(hd_url))
    if Picture_request.status_code == 200:
        with open("C:/Users/jmpst/Downloads/image.jpg", 'wb') as f:
            f.write(Picture_request.content)
            print("You got the HD image!")
else:
    print('Please wait..')
    Picture_request = requests.get('{}?api_key=sRkSnDSlvzNR4VVZpHh31vM83gNB1ndbeAANCoId'.format(pic_url))
    if Picture_request.status_code == 200:
        with open("C:/Users/jmpst/Downloads/image.jpg", 'wb') as f:
            f.write(Picture_request.content)
            print("You got the image!")



