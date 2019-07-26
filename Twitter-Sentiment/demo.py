import tweepy
from textblob import TextBlob
import csv

# Step 1 - Authenticate
consumer_key= 'JYcaS7LrGZMB9w6z4MvD5JiAa'
consumer_secret= 'ljyGM2ItUtPUTREWNZiMl7GJjLv84pBv7tx59jMzDRdrWzcbjG'

access_token= '2162673698-5dMo4aqZhwrvWDBwjhg3TrQW5QDfWZarbX5WnQk'
access_token_secret= 'DueMI2WMuK9Gy32T1Mqcedy8r5ysxstfkPCIgaIIhVAcm'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
name = 'Trump'
public_tweets = api.search(name)

def getSentiment(analysis):
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    else:
        return 'Negative'
        
#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself

with open(name+'.csv', 'w') as csvFile:
    for tweet in public_tweets:
        if 'RT @' not in tweet.text:
            analysis = TextBlob(tweet.text)
            data = [[tweet.user.screen_name, tweet.text, getSentiment(analysis)]]
            writer = csv.writer(csvFile)
            writer.writerows(data)
    csvFile.close()


    
    #Step 4 Perform Sentiment Analysis on Tweets
    # analysis = TextBlob(tweet.text)
    # print(analysis.sentiment)
    # print("")