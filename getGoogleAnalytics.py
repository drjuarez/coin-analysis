import requests
import json
import psycopg2
import pdb
from datetime import datetime
import time
import sys
from pytrends.request import TrendReq
from dbConnection import query_db

# r = requests.get(query_string)
# coins = r.json()
# database = "davidjuarez"
# host = "localhost"
# port ="5432"
# conn = psycopg2.connect(database=database, host=host, port=port)
# conn.autocommit = True
#
# query_string = 'https://api.coinmarketcap.com/v1/ticker/?start={}&limit={}'.format(start, collection_size)
#
# cur = conn.cursor()
# coin = coins[0]
# now = time.localtime()
# f = '%Y-%m-%d %H:%M:%S'
# timestamp = time.strftime(f, now)

query_result = query_db('select name from coins')
coin_names = [coin[0] for coin in query_result]

pytrend = TrendReq()
for coin in coin_names:
    # kw_list = [coin + " cryptocurrency"]
    kw_list = [coin]
    pytrend.build_payload(kw_list, cat=0, timeframe='today 3-m', geo='', gprop='')
    interest = pytrend.interest_over_time()
    pdb.set_trace()
    print(interest_over_time_df)
