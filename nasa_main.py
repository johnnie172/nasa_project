import requests, json, os, sys, time, threading
import input_utilities, utilities, loading_display_utilities, download_manger, request_utilities, consts


def main():
    if request_utilities.test_internet_connection():

        selected_date = input_utilities.get_date_from_user()
        response = request_utilities.check_url_response(consts.URL, consts.KEY, selected_date)
        # checking for code 200:
        if response:
            print(consts.CHECK_MEDIA_TYPE_MESSEGE)
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
                print(consts.NOT_SUPPORTING_VIDEO_MESSEGE)
                print(url_data["url"])
        else:
            print(consts.GENERIC_ERROR_MESSEGE)
            print('Response cods: {}'.format(response))


if __name__ == '__main__':
    main()
