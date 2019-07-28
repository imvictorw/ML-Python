import tweepy
import csv
import numpy as np
from textblob import TextBlob
from keras.models import Sequential
from keras.layers import Dense


#Step 1 - Insert your API keys
consumer_key= 'JYcaS7LrGZMB9w6z4MvD5JiAaL'
consumer_secret= 'ljyGM2ItUtPUTREWNZiMl7GJjLv84pBv7tx59jMzDRdrWzcbjG'
access_token= '2162673698-5dMo4aqZhwrvWDBwjhg3TrQW5QDfWZarbX5WnQk'
access_token_secret= 'DueMI2WMuK9Gy32T1Mqcedy8r5ysxstfkPCIgaIIhVAcm'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Step 2 - Search for your company name on Twitter
public_tweets = api.search('Apple')

#Step 3 - Define a threshold for each sentiment to classify each
#as positive or negative. If the majority of tweets you've collected are positive
#then use your neural network to predict a future price
overall = 0
threshold = 0
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    if analysis.sentiment.polarity >= threshold:
        overall+=1
    else:
        overall-=1

if overall > 0:
    print('Overall Positive')
else:
    print('Overall Negative')


#data collection
dates = []
prices = []
def get_data(filename):
	with open(filename, 'r') as csvfile:
		csvFileReader = csv.reader(csvfile)
		next(csvFileReader)
		for row in csvFileReader:
			if row[0] == '':
				break

			dates.append(int(row[0].split('/')[0]))
			prices.append(float(row[1]))
	return

#Step 5 reference your CSV file here
get_data('paststock.csv')

#Step 6 In this function, build your neural network model using Keras, train it, then have it predict the price
#on a given day. We'll later print the price out to terminal.
def predict_price(dates, prices, x):
    trainX = np.reshape(dates,(len(dates), 1)) # converting to matrix of n X 1
    trainY = np.reshape(prices,(len(prices), 1)) # converting to matrix of n X 1

    # Create and fit Multilinear Perceptron model
    model = Sequential()
    model.add(Dense(64,input_dim=1,activation='relu', kernel_initializer="uniform"))
    model.add(Dense(64,activation='relu', kernel_initializer="uniform"))
    model.add(Dense(1,activation='relu',kernel_initializer="uniform"))
    model.compile(optimizer='rmsprop',
              loss='mse')
    model.fit(trainX, trainY, epochs=200, batch_size=10)

    print(trainY)
    score = model.predict(trainY[x])
    return score

predicted_price = predict_price(dates, prices, 10)
print(predicted_price)
