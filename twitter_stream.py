try:
	import json
except:
	import simplejson as json
	
#from twitter import OAuth,TwitterHTTPError,TwitterStream

access_token = '3281272220-ALO2vwwFbTeLybsW5xBtq7Ftvjt27wT07awEeKF'
access_secret = 'C1X8CcWiMSSsnxqNnKvT6OjjqFPQfOhXCeUirpQCSfzRL'
consumer_key = 'smxlBnDA3Wtvww2sFasJrpAbP'
consumer_secret = 'i7Lps6KHHT6UhF1Eu09mcWA5JSmtN1DodEM0CMPuUpuyIc2XuM'

#oauth = OAuth(access_token,access_secret,consumer_key,consumer_secret)


#streaming API

"""
twitter_stream = TwitterStream(auth=oauth) 
iterator = twitter_stream.statuses.sample()

tweet_count = 10
for tweet in iterator:
	tweet_count -= 1
	print(json.dumps(tweet))
	
	if tweet_count <=0:
		break

"""

#Search API
"""
twitter = Twitter(auth = oauth)
p=twitter.search.tweets(q='#padmavati',result_type='recent'		)
print(p)
"""

#user API
#twitter = Twitter(auth = oauth)
#p = twitter.followers.ids(screen_name="MiaMalkova")
#print(len(p['ids']))

import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)

#followers
overall = []
s = ['moonlightmov','MBTSMovie','LaLaLand','keithmaitland','arrivalmovie','TheJungleBook','EdgeOf17','SullyMovie','LorenzoVigas','The_Green_Gold','thebeatles','DrStrange','','taleoftales','CaptainMovieUK','','HailCaesarMovie ‏','HacksawRidge‏','dontbreathe','','','','NateParker','justinlin','meeraonthewall','LoreneScafaria','PopstarMovie','DanielRagussis','','lastdesert','','barbershopmovie ‏','gilkenan','FantasticBeasts','InfiltratorMov','RogueOneMovie','whitegirl_movie','TheConjuring','deadpoolmovie','GoatMovie','The Eyes of My Mother ','DavidFarrUK','mshowalter','BleedForThis','','Ghostbusters','AlliedMovie','TumbledownMovie','BadMoms','']
s += ['IntoTheForest','ElvisNixonMovie','AbFabMovie ‏','jasonbourne','PlayNerve','','LightsOutMovie','SnowdenTheMovie','hologramforking','MichaelTougias ‏','','WTFTheMovie','MissPeregrinesHomeForPeculiarChildren']
s += ['Band_of_Robbers','wardogsmovie','','RaceMovie','','AlmostChristmas','Robburnett1','','','','HandsofStoneMov','EddieEagleMovie','AdamBaldwin','ProgramTheMovie', 'knightofcupsmov','','FreeStateMovie','','MrRightMovie','CentralIntel','XMenMovies','Triple9Movie','tnd_film','','desierto','RisenMovie','accountantmovie','','','','janegotagunfilm ‏','livebynight','13hours','girlontrainfilm','Morgan','JackReacher','DressmakerMovie','']
s += ['NYSMmovie','KillFriendsFilm','PPZmovie','MiraclesHeaven','BatmanvSuperman','AmPastoralMovie','EqualsTheMovie','officexmasparty','infernothemovie','TheBoyMovie','','','PassengersMovie','SuicideSquadWB','TMNTMovie ‏','','TheMechanic','BenHurMovie','','','AssassinsMovie‏','','TheHuntsman','','','ZoolanderMovie','DivergentSeries','RideAlong','ID4Sequel ‏','warcraftmovie','FSOBMovie','GodsofEgypt','CBeautyMovie','','ninelives','','LionMovie','HiddenFigures','amonstercalls']



print(len(s))
sf = []
for name in s:
	try:
		user = api.get_user(name)
		l = user.followers_count
		print(l)
		sf.append(l)
	except:
		print('escape')
		sf.append(0)
	

