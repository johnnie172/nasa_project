import requests, json


def check_url_response(url, key, date):
    return requests.get(url.format(key, date))


def get_data_from_respone(response):
    return json.loads(response.text)