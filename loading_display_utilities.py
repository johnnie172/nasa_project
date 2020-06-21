import time
from termcolor import colored, cprint


def show_loader(input):
    loading1 = colored('Loading.', 'red', attrs=['reverse', 'blink'])
    loading2 = colored('.', 'red', attrs=['reverse', 'blink'])
    loading3 = colored('.', 'red', attrs=['reverse', 'blink'])
    loading4 = colored('.', 'red', attrs=['reverse', 'blink'])
    loading5 = colored('.', 'red', attrs=['reverse', 'blink'])

    loading_lst = [loading1, loading2, loading3, loading4, loading5]
    while input != True:

        for load in loading_lst:
            print(load, end='')
            time.sleep(1)

        break
