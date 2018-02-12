import json, twitter_conf
from twitter import Twitter, OAuth

search_word = 'twitter'

t = Twitter(auth=OAuth(
  twitter_conf.ACCESS_TOKEN,
  twitter_conf.ACCESS_TOKEN_SECRET,
  twitter_conf.CONSUMER_KEY,
  twitter_conf.CONSUMER_SECRET
))

searched_tweets = t.search.tweets(q = search_word)
print(searched_tweets)
