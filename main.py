import tweepy
import textblob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import yaml

keys=yaml.safe_load(open('twitterkeys.yaml'))

config_OAuth=[
    keys['API_key'],
    keys['API_key_secret']
]

config_AccessToken=[
    keys['access_token'],
    keys['access_token_secret']
]

authenticator = tweepy.OAuthHandler(*config_OAuth)
authenticator.set_access_token(*config_AccessToken)

api =tweepy.API(authenticator, wait_on_rate_limit=True)

crypto_currency = 'tesla'

search = f'#{crypto_currency} -filter:retweets'

tweet_cursor = tweepy.Cursor(api.search, q=search, lang='en', tweet_mode='extended').items(100)

tweets=[tweet.full_tyext for tweet in tweet_cursor]

tweets.df = pd.DataFrame(tweets, columns=['Tweets'])





