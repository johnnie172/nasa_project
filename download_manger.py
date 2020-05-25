import utilities, loading_display_utilities, nasa_main
import threading


def start_download(selected_quality):
    x = threading.Thread(target=utilities.pic_downloader, args=(selected_quality,))
    y = threading.Thread(target=loading_display_utilities.show_loader, args=(x,))
    z = threading.Thread(target=utilities.checking_file_size)
    x.start()
    y.start()
    x.join()
    loading_display_utilities.show_loader(False)
    z.start()
