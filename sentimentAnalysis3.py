# Text-Processing Sentiment Analysis

import requests

url = "http://text-processing.com/api/sentiment/"

payload = {'text': 'Today is going to be great!'}

response = requests.request("POST", url, data=payload)

print(response.text)
