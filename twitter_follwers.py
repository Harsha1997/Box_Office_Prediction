try:
    import json
except:
    import simplejson as json

import tweepy
import csv
import pandas as pd


access_token = '3281272220-ALO2vwwFbTeLybsW5xBtq7Ftvjt27wT07awEeKF'
access_secret = 'C1X8CcWiMSSsnxqNnKvT6OjjqFPQfOhXCeUirpQCSfzRL'
consumer_key = 'smxlBnDA3Wtvww2sFasJrpAbP'
consumer_secret = 'i7Lps6KHHT6UhF1Eu09mcWA5JSmtN1DodEM0CMPuUpuyIc2XuM'



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
public_tweets = api.home_timeline()

follow = []
change_data = pd.read_csv('train.csv')

for name in change_data['twitter_handles'] :
	try :
		name = name.strip()
		user = api.get_user(name)
		printt = user.followers_count
		follow.append(printt)
		print(printt)
	except:
		follow.append(0)
		
count = pd.Series(follow)
change_data['followers_count'] = count.values
change_data.to_csv('train_data.csv')
print(change_data['followers_count'])
	


