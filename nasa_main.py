import requests, json, os, sys, time, threading
import input_utilities, utilities, loading_display_utilities, download_manger, request_utilities, consts


def main():
    selected_date = input_utilities.get_date_from_user()
    url = consts.url
    response = request_utilities.check_url_response(url, consts.key, selected_date)
    # checking for code 200:
    if response:
        print(consts.check_madia_type_messege)
        # Getting the url dict:
        url_data = request_utilities.get_data_from_respone(response)
        # Checking for media type:
        if utilities.check_for_media_type(url_data):
            # Making text file with pic explanation:
            utilities.make_explanation_text_file(url_data)
            # Asking for quality to download:
            selected_quality = input_utilities.get_quality_from_user(url_data)
            download_manger.start_download(selected_quality)
        else:
            print(consts.not_supporting_video_messege)
            print(url_data["url"])
    else:
        print(consts.generic_error_messege)
        print('Response cods: {}'.format(response))


if __name__ == '__main__':
    main()
