from bittrex import Bittrex
import requests
import json
import pandas as pd
import pdb
import utility
from dbConnectionLocal import query_db

key = '022a53e30bb44c63b3caf23f2fb2a040'
secret = 'a4d79f5c70b14a20879c94aeca58e763'
bx_api = Bittrex(key, secret)

def get_tickers():
    query_result = query_db('select ticker from coins')
    return [coin[0] for coin in query_result]

def seed_coins(start, collection_size):
    coin_market_cap_ep = 'https://api.coinmarketcap.com/v1/ticker/?start={}&limit={}'.format(start, collection_size)
    r = requests.get(coin_market_cap_ep)
    return r.json()

def get_historical_data(ticker, days):
    historicals_ep = 'https://min-api.cryptocompare.com/data/histoday?fsym={}&tsym=USD&limit={}&aggregate=3&e=CCCAGG'.format(ticker, days)
    r = requests.get(historicals_ep)
    return r.json()["Data"]

def get_bittrex_balance():
    return bx_api.get_balances()['result']

def find_exchange_rate(from_ticker, to_ticker, on_date):
    timestamp = utility.unix_timestamp_on(on_date)
    price_ep = 'https://min-api.cryptocompare.com/data/pricehistorical?fsym={}&tsyms={}&ts={}&extraParams=your_app_name'.format(from_ticker, to_ticker, timestamp)
    return requests.get(price_ep).json()[from_ticker][to_ticker]

def calculate_average_price(coins):
    orders = pd.read_excel('fullOrders.xls')
    orders.loc[:] = orders.loc[orders.loc[:, 'Type'] == 'LIMIT_BUY']

    for i, row in orders.iterrows():
        print(row)
        purchase_coin = row['Exchange'].split('-')[1]
        purchase_date = row['Closed'].strftime('%d-%m-%y %H:%M:%S')
        row['priceUsd'] = find_exchange_rate(purchase_coin, 'USD', purchase_date)

    pdb.set_trace()
