from binance.client import Client
from binance.enums import *
from src.BinanceKeys import BinanceKey1
from datetime import datetime
import time
import os
import json
import requests
from urllib.request import urlopen

api_key = BinanceKey1['api_key']
api_secret = BinanceKey1['api_secret']
os.system('clear')
print('Connecting to BINANCE...')
client = Client(api_key, api_secret)
print('status : Connected.')
BLYNK_AUTH = '9HIeo403qLUzAKi5UYIpCCiAy7C7nJeK'
url = 'http://blynk-cloud.com/' + BLYNK_AUTH 


def update(pin, value):
    payload = url + '/update/' + pin + '?value=' + str(value)
    requests.get(payload)
    print(payload)
    
def get_delta(symbol1, symbol2):
    tickers = client.get_all_tickers()
    asset1 = next(item for item in tickers if item['symbol'] == symbol1)['symbol']
    price1 = float(next(item for item in tickers if item['symbol'] == symbol1)['price'])
    asset2 = next(item for item in tickers if item['symbol'] == symbol2)['symbol']
    price2 = float(next(item for item in tickers if item['symbol'] == symbol2)['price'])
    delta = round((price2 - price1),2)
    print(asset1, ':', price1)
    print(asset2, ':', price2)
    print('delta :', delta)
    return(delta)

while True:
    delta = get_delta('LTCUSDT', 'XMRUSDT')
    update('v1',delta)

    if delta > 2:
        print('sell XMR -> buy LTC')

    elif delta < 1:
        print('sell LTC -> buy XMR')

    time.sleep(0.1)
    os.system('clear')


'''

XMR - LTC > 2   then    sell XMR -> buy LTC
XMR - LTC < 1   then    sell LTC -> buy XMR

'''

