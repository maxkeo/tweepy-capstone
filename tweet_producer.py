#!/usr/bin/python3 

from kafka import KafkaProducer
from datetime import datetime
import tweepy
import sys
import re

consumer_key = "dxjQapAQkTTmGBRzWsjCdxwQs"
consumer_secret_key = "R0H4sJMO6llGDz66pejGCNgpR1RrdL82DSGnVFCUktvLHwCDIv"

access_token = "1305547265004589056-YuQEGDsUkyb4zHShfKh4SOz6rJUl9v"
access_token_secret = "4OMkO1qFibMfiohugSIbHWDE7oYdQdyTFygTedp2nC27z"

TWEET_TOPICS = ['bitcoin, ethereum, cardano, solana, avalanche']

KAFKA_BROKER = 'localhost:9092'
KAFKA_TOPIC = 'tweets'

class Streamer(tweepy.StreamListener):

	def on_error(self, status_code):
		if status_code == 402:
			return False

	def on_status(self, status):
		tweet = status.text
		full_tweet = status.user.screen_name + tweet;
		print(status.user.screen_name,status.text)

		tweet = re.sub(r'RT\s@\w*:\s', '', tweet)

		global producer
		producer.send(KAFKA_TOPIC, bytes(full_tweet, encoding='utf-8'))

		d = datetime.now()

		print(f'[{d.hour}:{d.minute}.{d.second}]')
		
		print("===========================================================")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

streamer = Streamer()
stream = tweepy.Stream(auth=api.auth, listener=streamer)

try:
    producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER)
except Exception as e:
    print(f'Error Connecting to Kafka --> {e}')
    sys.exit(1)

stream.filter(track=TWEET_TOPICS)
