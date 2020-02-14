from binance.client import Client
from binance.enums import *
from src.BinanceKeys import BinanceKey1
from datetime import datetime
import time
import os
import json
import requests

api_key = BinanceKey1['api_key']
api_secret = BinanceKey1['api_secret']

os.system('clear')
print('Connecting to BINANCE...')
client = Client(api_key, api_secret)
print('connected.')

def get_bitkub():
    url = "https://api.bitkub.com/api/market/ticker"
    # print ("Request JSON from : " + url)
    response = requests.get(url)
    data = response.json()
    asset = 'THB_BTC'
    price = float(data["THB_BTC"]["last"])
    # print('\nBITKUB')
    # print(asset, ':', price)
    return(price)

def get_binance():
    tickers = client.get_all_tickers()
    asset = next(item for item in tickers if item['symbol'] == 'BTCUSDT')['symbol']
    price = float(next(item for item in tickers if item['symbol'] == 'BTCUSDT')['price']) * 31.15
    # print('\nBINANCE')
    # print(asset, ':', price)
    return(price)

def history_update(balance):
    now             = datetime.now()
    current_time    = now.strftime("%Y%m%d,%H:%M:%S")
    balance         = str(balance)
    payload         = 'python3 ./google/append2gsheet.py --data ' + current_time + ',' + str(balance) + ' --sheetid 1uxG4YKI2v5tb-ZJkWvX58t8FdHmx93xAmhEnXeB9SRA --range "' + 'history' + '" --noauth_local_webserver'
    os.system(payload)

while True:
    try:
        bitkub = get_bitkub()
        binance = get_binance()
        ratio1 = (binance-bitkub)/bitkub*100
        ratio2 = (bitkub-binance)/binance*100
        delta = bitkub-binance

        os.system('clear')

        if bitkub < binance:
            print('BITKUB   ->  BINANCE')
        elif bitkub > binance:
            print('BINANCE  ->  BITKUB')
        print('\ndelta :', abs(delta))
        print('ratio1 :', ratio1)
        print('ratio2 :', ratio2)
        history_update(delta)
        time.sleep(0.5)

    except Exception as e:
        print(e)
    
