import requests
import json
import pdb
from datetime import datetime
import time
import sys
from dbConnection import query_db


start = sys.argv[1]
collection_size = sys.argv[2]
query_string = 'https://api.coinmarketcap.com/v1/ticker/?start={}&limit={}'.format(start, collection_size)

r = requests.get(query_string)
coins = r.json()
now = time.localtime()
date_format = '%Y-%m-%d %H:%M:%S'
timestamp = time.strftime(date_format, now)

for coin in coins:
    statement = 'INSERT INTO public.coins(name, ticker, rank, price, market_cap, volume, created_at) \
    VALUES (\'{}\', \'{}\', {}, {}, {}, {}, \'{}\')' \
    .format(coin['name'], coin['symbol'], coin['rank'], coin['price_usd'], coin['market_cap_usd'], coin['24h_volume_usd'], timestamp)

    query_db(statement)
