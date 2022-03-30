import threading
import requests
import time

    tokens = open("tokens.txt", "r").read().splitlines()
    channel = input('CHANNEL ID: ')
    mess = input('MESSAGE: ')
    delay = input('Delay: ')

    for token in tokens:
        time.sleep(int(delay))
        threading.Thread(target=spam, args=(token, channel_id, text)).start()
        
