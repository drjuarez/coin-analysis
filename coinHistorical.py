import requests
import json
import pdb
from datetime import datetime
import time
import sys
from dbConnectionLocal import query_db
import Calculator
import pandas as pd
import utility
import CoinSource

# start = sys.argv[1]
# collection_size = sys.argv[2]
STRING_FORMAT = '%Y-%m-%d'
HISTORICAL_DAYS = 90
intervals = [3, 5, 7, 30, HISTORICAL_DAYS]

#
# This gets top 100 coins: CoinSource.get_coins(1, 100)
# Will write all the coins to db
#   timestamp = utility.timestamp_for_db()
    # for coin in coins:
    #     statement = 'INSERT INTO public.coins(name, ticker, rank, price, market_cap, volume, created_at) \
    #     VALUES (\'{}\', \'{}\', {}, {}, {}, {}, \'{}\')' \
    #     .format(coin['name'], coin['symbol'], coin['rank'], coin['price_usd'], coin['market_cap_usd'], coin['24h_volume_usd'], timestamp)
    #     query_db(statement)

# query for writing the historical data

tickers = coinSource.get_tickers()

for ticker in tickers:
    historical_data = CoinSource.get_historical_data(ticker, HISTORICAL_DAYS)
    hist_df = pd.DataFrame(historical_data)
    calcs = Calculator.run_calculations(hist_df.loc[:,'close'], intervals)
    calcs_and_history = hist_df.join(calcs)

    jsons = []
    for row in calcs_and_history.iterrows():
        json_row = row[1].to_json()
        jsons.append(json_row)

    date_string = utility.timestamp_for_db()
    query_string = 'UPDATE coins set historical = array{}::jsonb[], created_at = \'{}\' where ticker = \'{}\''.format(jsons, date_string, ticker)
    query_db(query_string, fetch=False)
