
from tweepy.streaming import Stream 
from tweepy.auth import OAuthHandler
from tweepy.streaming import StreamListener



access_token = "3390463630-oLqK3Os0yzNmPMFrz3RDP23qFwhZh8LpprSwXIk"
access_token_secret = "7NwTsd1zM6pZLFY9k4cHYrgDnM3y4bVOOUhjRTqjSKcrd"
consumer_key = "gZ4RLY9JHTuGObfPXBb4MgeZy"
consumer_secret = "qZxtJgsGXxCkAMg8dVeI0wN0V0g0b9WcrQaXqXvpN7Zu7MWb2U"

#This is a basic listener that prints received tweets to stdout 
class StdOutListner(StreamListener):
	def on_data(self,data):
		print data 
		return True 

	def on_error(self, status):
		print status

if __name__ == '__main__':

	#This handles twitter authentification and the connection to Twitter Streaming API 
	listener=StdOutListner()
	#Handles the authorization 
	auth = OAuthHandler(consumer_key,consumer_secret)
	#Sets the access tokens 
	auth.set_access_token(access_token, access_token_secret)
	#Stream the data from the authorization  guy to the listener 
	stream = Stream(auth, listener)

	stream.filter(track=['python','javascript','ruby'])