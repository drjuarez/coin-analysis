import pdb
from datetime import date, timedelta
from pytrends.request import TrendReq
from dbConnection import query_db
import pandas as pd
import numpy as np

preceding_days = 31
# prep dataframe: Grabbing for last 30 days
starting_date = date.today() - timedelta(days=preceding_days)
starting_date_string = date.strftime(starting_date, '%Y%m%d')
dates = pd.date_range(starting_date_string, periods=preceding_days)
trend_df = pd.DataFrame(index=dates)
# pdb.set_trace()

query_result = query_db('select name from coins')
coin_names = [coin[0] for coin in query_result]
pytrend = TrendReq()
for coin in coin_names:
    # kw_list = [coin + " cryptocurrency"]
    kw_list = [coin]
    pytrend.build_payload(kw_list, cat=0, timeframe='today 1-m', geo='', gprop='')
    coin_interest = pytrend.interest_over_time()
    del coin_interest['isPartial']
    trend_df = pd.merge(trend_df, coin_interest, how='left', left_index=True, right_index=True)


    # for index,row in interest.iterrows():
    #     print (index)
        # print (row[2])
