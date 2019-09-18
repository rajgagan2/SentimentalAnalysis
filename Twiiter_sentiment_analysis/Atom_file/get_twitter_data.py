#!/usr/bin/python
import tweepy
import csv #Import csv
import os
import twitter_credentials
import time

start_time = time.clock()

# Consumer keys and access tokens, used for OAuth
consumer_key = twitter_credentials.CONSUMER_KEY
consumer_secret = twitter_credentials.CONSUMER_SECRET
access_token = twitter_credentials.ACCESS_TOKEN
access_token_secret = twitter_credentials.ACCESS_TOKEN_SECRET

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Open/Create a file to append data
csvFile = open('Twitter_data_sabrimalai_issue_2.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

ids = set()

tags = ["SabkaSabarimalaTemple","savesabarimala"]
for tag in tags:
    for tweet in tweepy.Cursor(api.search,q=tag,lang="en",rpp=100).items(200):
        if (not tweet.retweeted) and ('RT @' not in tweet.text):
            #Write a row to the csv file/ I use encode utf-8
            csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'), tweet.favorite_count, tweet.retweet_count, tweet.id, tweet.user.screen_name])
            #print "...%s tweets downloaded so far" % (len(tweet.id))
            ids.add(tweet.id) # add new id
            print ("number of unique ids seen so far: {}",format(len(ids)))
csvFile.close()
print("data Collection is done")
end_time = time.clock()-start_time
print("Total time taken for programme to complete {} seconds".format(end_time))
