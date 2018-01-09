import praw
import pdb
import pprint
from datetime import datetime
import re
from collections import Counter

# Global
# ------------------------------
NUMBER_OF_POSTS=10
SUBREDDITS = ['cryptocurrencies', 'cryptomarkets','altcoin']

# Reddit API
r = praw.Reddit(client_id='kOTul76pBBTGLA',
                     client_secret='dgDZ-iWlVCEoihbP2oLz66e-Q3A',
                     password='tothemoon123',
                     user='getrichaf',
                     user_agent='coin analysis bot by /u/getsdfsdfafrichaf')

# ------------------------------

def get_top_comments(subreddit):
    sr = r.subreddit(subreddit)
    i=0
    # TODO: catch errors thrown from dropped connection
    for post in sr.hot(limit=NUMBER_OF_POSTS):
        # Flatten all the comments
        post.comments.replace_more(limit=None)

        for comment in post.comments.list():
            print(comment)

start_time = datetime.now()

# ------------------------------

def re_find_func(patterns,phrase):
    '''
    Take in a list of patterns
    Returns list of matches
    '''
    tickers_list = []

    for pattern in patterns:
        ticker = re.findall(pattern,phrase)

        for item in ticker:
            item = item.strip('.!? ')
            tickers_list.append(item)

    return tickers_list

# START HERE--------

# Steps:
# 1- Create a default dictionary (data structure that counts each of the mentions from the ticker )
# 2- Create a regular expression that grabs any group of capital letters (either 2 or 3 or 4 capitalized letters)
# 3- Iterate throguh each of the subreddits and call get_top_comments() on each subreddit
# 4- Update the get_top_comments inner for loop function to pass the comment body
#     to the regex created in step 2.  If regex passes; store in default dictionary in step 1
# ** Final Result should be a dictionary with tickers as the keys and the count each ticker was mentioned in the body.

# Begin iterating through each of the SUBREDDITS here and call get_top_comments function for each subreddit
# e.g. Below

example = 'These are the tickers that I am trying to find: IOTA. BTC ETH! BTC BTC LTC ETH ETH XLM IOTA! XRB LSMR'

ticker_pat = [r'\b[A-Z]{3,4}\b[.!?]?'] # grabs all tickers with 3 or 4 capital letters

tickers = re_find_func(ticker_pat,example)
ticker_count = dict(Counter(tickers))
print(ticker_count)

#for i in SUBREDDITS:
#    top_comments = get_top_comments(i)
#    tickers = re_find_func(ticker_pat,top_comments)
#    ticker_count = dict(Counter(tickers))

print(datetime.now() - start_time)
