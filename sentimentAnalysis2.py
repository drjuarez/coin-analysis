# Aylien Sentiment Analysis

#-----------------------------
# First use pip install --upgrade aylien-apiclient
# API Documentation - https://docs.aylien.com/docs/introduction
#-----------------------------

from aylienapiclient import textapi

client = textapi.Client("731d3010", "b14456c61fa241a567df725d12801a2c")

sentiment = client.Sentiment({'text': 'John is a very good football player!'})
