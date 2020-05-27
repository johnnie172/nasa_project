import requests, json, consts, urllib.request


def test_internet_connection(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        print(consts.INTERNET_CONNECTION_OK_MESSEGE)
        return True
    except:
        print(consts.INTERNET_CONNECTION_FAIL_MESSEGE)
        return False


def check_url_response(url, key, date):
    try:
        response = requests.get(url.format(key, date))

        return response
    except Exception:
        print(consts.GENERIC_ERROR_MESSEGE)

    # except HTTPSConnection:
    #     print(consts.GENERIC_ERROR_MESSEGE)


def get_data_from_respone(response):
    return json.loads(response.text)
