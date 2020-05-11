import requests
import ast
key = 'sRkSnDSlvzNR4VVZpHh31vM83gNB1ndbeAANCoId'

response = requests.get('https://api.nasa.gov/planetary/apod?api_key=sRkSnDSlvzNR4VVZpHh31vM83gNB1ndbeAANCoId')
response_text = response.text
if response:
    print('**Success!!')

else:
    print('An error has occurred.')
    print('Response cods: {}'.format(response))


response_dir = ast.literal_eval(response_text)
assert type(response_dir) is dict

hdurl = response_dir["hdurl"]


user_input = input("Would you like to get the pic of today? ").lower()
if user_input[0] == 'y':
    Picture_request = requests.get('{}?api_key=sRkSnDSlvzNR4VVZpHh31vM83gNB1ndbeAANCoId'.format(hdurl))
    if Picture_request.status_code == 200:
        with open("C:/Users/jmpst/Downloads/image.jpg", 'wb') as f:
            f.write(Picture_request.content)
            print("You got the image!")
