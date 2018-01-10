import praw
import pdb
import pprint
from datetime import datetime
import re
from collections import Counter
import pandas as pd
import utility

# Global
# ------------------------------
NUMBER_OF_POSTS=10
# grabs all tickers with 3 or 4 capital letters
REGEX = [r'\b[A-Z]{3,4}\b[.!?]?']
SUBREDDITS = ['cryptocurrencies', 'cryptomarkets','altcoin']

# Reddit API
r = praw.Reddit(client_id='kOTul76pBBTGLA',
                     client_secret='dgDZ-iWlVCEoihbP2oLz66e-Q3A',
                     password='tothemoon123',
                     user='getrichaf',
                     user_agent='coin analysis bot by /u/getrichaf')

# =================================

def get_tickers_from(subreddit):
    sr = r.subreddit(subreddit)
    tickers_in_subreddit = []

    # TODO: catch errors thrown from dropped connection
    for post in sr.hot(limit=NUMBER_OF_POSTS):
        try:
            # Flatten all the comments
            post.comments.replace_more(limit=None)

            for comment in post.comments.list():
                tickers_in_subreddit.append(use_regex(REGEX, comment.body))
        except Exception, e:
            print('we done fooged', e)
            continue
    return tickers_in_subreddit

def use_regex(patterns,phrase):
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



# Main
# ------------------------------
# Steps:
# 1- Create a default dictionary (data structure that counts each of the mentions from the ticker )
# 2- Create a regular expression that grabs any group of capital letters (either 2 or 3 or 4 capitalized letters)
# 3- Iterate throguh each of the subreddits and call get_top_comments() on each subreddit
# 4- Update the get_top_comments inner for loop function to pass the comment body
#     to the regex created in step 2.  If regex passes; store in default dictionary in step 1
# ** Final Result should be a dictionary with tickers as the keys and the count each ticker was mentioned in the body.

# Begin iterating through each of the SUBREDDITS here and call get_top_comments function for each subreddit
# e.g. Below


start_time = datetime.now()
ticker_array = []

for subreddit in SUBREDDITS:

    tickers_from_comments = get_tickers_from(subreddit)
    # Flatten out array
    ticker_array.append([item for sublist in tickers_from_comments for item in sublist])

flattened_ticker_array = [item for sublist in ticker_array for item in sublist]
ticker_count = dict(Counter(flattened_ticker_array))
ticker_df = pd.Series(ticker_count, name='count')
ticker_df.to_csv('tickerCounts.csv')
pdb.set_trace()

print('script execution:', datetime.now() - start_time)


# get_top_comments('altcoin')
