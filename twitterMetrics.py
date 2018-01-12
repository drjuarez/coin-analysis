import requests
import json

r = requests.get('https://api.twitter.com/1.1/search/tweets.json?l=&q=cryptocurrency%2C%20OR%20blockchain%2C%20OR%20crypto&src=typd')

print(r.status_code)

#r.json()
