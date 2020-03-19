# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from binance.client import Client
from binance.enums import *
from src.BinanceKeys import BinanceKey1
from datetime import datetime
import time
import os
import json
import requests
from urllib.request import urlopen

BLYNK_AUTH = '9HIeo403qLUzAKi5UYIpCCiAy7C7nJeK'
url = 'http://blynk-cloud.com/' + BLYNK_AUTH 
api_key = BinanceKey1['api_key']
api_secret = BinanceKey1['api_secret']
os.system('clear')

print('Connecting to BINANCE...')
client = Client(api_key, api_secret)
print('status : Connected.')


# %%
def float2str(amount):
    precision = 5
    amt_str = "{:0.0{}f}".format(amount, precision)
    return amt_str

def update(pin, value):
    payload = url + '/update/' + pin + '?value=' + str(value)
    urlopen(payload)
    print(payload)

def check_balance():
    print('----balance----')
    balance_usdt = float(client.get_asset_balance(asset='USDT')['free'])
    balance_xmr  = float(client.get_asset_balance(asset='XMR')['free'])
    balance_ltc  = float(client.get_asset_balance(asset='LTC')['free'])
    print('USDT :', balance_usdt, '\nXMR :', balance_xmr, '\nLTC :', balance_ltc)
    update('v2',balance_usdt)
    update('v3',balance_xmr)
    update('v4',balance_ltc)
    return balance_usdt, balance_xmr, balance_ltc

def get_delta(symbol1, symbol2):
    tickers = client.get_all_tickers()
    asset1 = next(item for item in tickers if item['symbol'] == symbol1)['symbol']
    price1 = float(next(item for item in tickers if item['symbol'] == symbol1)['price'])
    asset2 = next(item for item in tickers if item['symbol'] == symbol2)['symbol']
    price2 = float(next(item for item in tickers if item['symbol'] == symbol2)['price'])
    delta = round((price1 - price2),2)
    print('\n----rate----')
    print(asset1, ':', price1)
    print(asset2, ':', price2)
    print('delta :', delta)
    update('v1',delta)
    return delta, price1, price2

def XMRtoLTC():
    check_balance()
    delta, rate_xmrusdt, rate_ltcusdt = get_delta('XMRUSDT', 'LTCUSDT')
    # XMR to USDT
    amt = round(float(client.get_asset_balance(asset='XMR')['free'])*0.999,5)
    while True:
        try:
            print('trading : {} XMR -> USDT'.format(amt))
            client.order_market_sell(symbol='XMRUSDT', quantity=amt)
            print('status : finish')
            break

        except:
            amt = round(amt*0.999,5)

    # USDT to LTC
    amt = round((float(client.get_asset_balance(asset='USDT')['free']))/rate_ltcusdt*0.999,5)
    while True:
        try:
            print('trading : {} USDT -> LTC'.format(amt))
            client.order_market_buy(symbol='LTCUSDT', quantity=amt)
            print('status : finish\n')
            break

        except:
            amt = round(amt*0.999,5)
    check_balance()
    
def LTCtoXMR():
    check_balance()
    delta, rate_xmrusdt, rate_ltcusdt = get_delta('XMRUSDT', 'LTCUSDT')
    # LTC to USDT
    amt = round(float(client.get_asset_balance(asset='LTC')['free'])*0.999,5)
    while True:
        try:
            print('trading : {} LTC -> USDT'.format(amt))
            client.order_market_sell(symbol='LTCUSDT', quantity=amt)
            print('status : finish')
            break

        except:
            amt = round(amt*0.999,5)

    # USDT to XMR
    amt = round((float(client.get_asset_balance(asset='USDT')['free']))/rate_xmrusdt*0.999,5)
    while True:
        try:
            print('trading : {} USDT -> XMR'.format(amt))
            client.order_market_buy(symbol='XMRUSDT', quantity=amt)
            print('status : finish\n')
            break

        except:
            amt = round(amt*0.999,5)
    check_balance()


# %%
while True:
    try:
        usdt, xmr, ltc = check_balance()
        delta, rate_xmrusdt, rate_ltcusdt = get_delta('XMRUSDT', 'LTCUSDT')
        if delta > 2.3 and ltc < xmr:
            XMRtoLTC()
        elif delta < 1.3 and ltc > xmr:
            LTCtoXMR()
        else:
            print('nothing.')
        os.system('clear')
    except Exception as e:
        print('ERROR :', e)
        


