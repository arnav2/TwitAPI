from tweepy.streaming import Stream 
from tweepy.auth import OAuthHandler
from tweepy.streaming import StreamListener
import json 
import pandas as pd 
import os 
import matplotlib.pyplot as plt

access_token = "3390463630-oLqK3Os0yzNmPMFrz3RDP23qFwhZh8LpprSwXIk"
access_token_secret = "7NwTsd1zM6pZLFY9k4cHYrgDnM3y4bVOOUhjRTqjSKcrd"
consumer_key = "gZ4RLY9JHTuGObfPXBb4MgeZy"
consumer_secret = "qZxtJgsGXxCkAMg8dVeI0wN0V0g0b9WcrQaXqXvpN7Zu7MWb2U"



#This is a basic listener that prints received tweets to stdout 
class StdOutListner(StreamListener):
	
	def on_data(self,data):
		#tweets_file = open("twitter.txt", 'a') 
		#tweets_file.write(data)
		#tweets_file.close()
		with open ("twitter.txt",'a') as f: 
			json.dump(data,f)
		#print data 


		return True 

	def on_error(self, status):
		print "shit"
		#print status
def readtweets():
	tweets_data = []
	tweets_file = open("twitter.txt", 'r')
	for line in tweets_file:
		try:
			tweet=json.loads(line)
			tweets_data.append(tweet)
		except:
			continue
	print len(tweets_data) 
	tweets = pd.DataFrame()
	tweets['text'] = map(lambda tweet: tweet['text'],tweets_data)
	tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
	tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
	tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)

	tweets_by_lang = tweets['lang'].value_counts()

	fig, ax = plt.subplots()
	ax.tick_params(axis='x', labelsize=15)
	ax.tick_params(axis='y', labelsize=10)
	ax.set_xlabel('Languages', fontsize=15)
	ax.set_ylabel('Number of tweets' , fontsize=15)
	ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
	tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')
	
if __name__ == '__main__':
	print "1"
	#This handles twitter authentification and the connection to Twitter Streaming API 
	listener=StdOutListner()
	#Handles the authorization 

	print "2"
	auth = OAuthHandler(consumer_key,consumer_secret)
	#Sets the access tokens 
	auth.set_access_token(access_token, access_token_secret)
	#Stream the data from the authorization  guy to the listener 
	stream = Stream(auth, listener)
	print "3"
	#stream.filter(track=['python','javascript','ruby'])

	readtweets()

