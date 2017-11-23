# Paramaters
# =========================
export start_position=100
export number_of_coins=10


# =========================
# Go to Coin Market cap and scrape 100 coins
python3 ./getCoins.py $start_position $number_of_coins

# for each of the coins in the database, get google analytics trending
