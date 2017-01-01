import json 
import pandas as pd 
import os 
import twitpy 
#Later use plotly to show this data in real time 
#import matplotlib.pyplot as plt
class readtweets():
	tweets_data = []
	tweets_file = open("twitter.txt", 'r')
	for line in tweets_file:
		try:
			tweet=json.loads(line)
			tweets_data.append(tweet)
		except:
			continue
	print len(tweets_data)

