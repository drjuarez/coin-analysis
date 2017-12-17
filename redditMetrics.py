import praw
import pdb
import pprint
from datetime import datetime

# Global
# ------------------------------
NUMBER_OF_POSTS=500
SUBREDDITS = ['cryptocurrencies', 'cryptomarkets','altcoin' ]

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

# START HERE--------

# Steps:
# 1- Create a default dictionary (data structure that counts each of the mentions from the ticker )
# 2- Create a regular expression that grabs any group of capital letters (either 2 or 3 or 4 cpaitalized letters)
# 3- Iterate throguh each of the subreddits and call get_top_comments() on each subreddit
# 4- Update the get_top_comments inner for loop function to pass the comment body
#     to the regex created in step 2.  If regex passes; store in default dictionary in step 1
# ** Final Result should be a dictionary with tickers as the keys and the count each ticker was mentioned in the body.



# Begin iterating through each of the SUBREDDITS here and call get_top_comments function for each subreddit
# e.g. Below
get_top_comments('altcoin')


print(datetime.now() - start_time)
