import tweepy
import csv
import json

# Twitter API credentials

consumer_key = 'vujZ19s53rDc8abpIDsrqavSV'
consumer_secret = 'JZaB1EgUSXEkzQ2gIE6pQEgbTCOYD1DB2426jwvXAYxWALY90F'
access_key = '2153140267-WDN6WMN3KQYpwWXCFQeNkbuyQod0tZgR2cZOU0P'
access_secret = 'lv4u2ynz6Ekn08Y9pIu0ohNPI0pZIvl1S98yyd26TjXfj'

# Create the api endpoint

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)
snance=[]
# Mention the maximum number of tweets that you want to be extracted.

maximum_number_of_tweets_to_be_extracted = \
int(input('Enter the number of tweets that you want to extract- '))

# Mention the hashtag that you want to look out for

user_mentions = "Maruti_Corp"

for tweet in tweepy.Cursor(api.search, q='@' + user_mentions,
rpp=100).items(maximum_number_of_tweets_to_be_extracted):
        snan={}
        if 'RT @' not in str(tweet.text.encode('utf-8')):
                snan['review']=str(tweet.text.encode('utf-8'))
                snance.append(snan)
                with open('scrt.json', 'w', encoding='utf-8') as f:
                        json.dump(snance, f, ensure_ascii=False, indent=4)

print ('Extracted ' + str(maximum_number_of_tweets_to_be_extracted) \
+ ' tweets with hashtag @' + user_mentions)
