# Paramaters
# =========================
export start_position=100
export number_of_coins=10


# =========================
# Go to Coin Market cap and scrape 100 coins
python3 ./getCoins.py $start_position $number_of_coins

#  - Collect Datasets
#  --------------------
# for each of the coins in the database:
#   - CryptoCompare: previous 30 days: 1- prices; 2- volume; 3- volatility
#   - Twitter: Number of mentions; Hashtag Hits
#   - Reddit: Subreddit Followers; Number of mentiosn on other subreddits (crypomarkets /  Cryptocurency' / Ethtrader)




#  - Backtesting / Validation
#  --------------------
#  Alphalens / Quantopian / ML
