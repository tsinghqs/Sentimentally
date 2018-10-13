import tweepy

#TextBlob is a Python Natural Language Processing Library
from textblob import TextBlob

#Twitter API keys and tokens to be used for Tweepy API
consumer_key = 'TCNvmZhcLVgG66ktybasO6ZZQ'
consumer_secret = '4n1AaDp8oSWMxJLaSz35WBlLuLgsyF7Xu8RYbfJAOkfBSy2UQF'
access_token = '2607970348-zbW69Qxp55mHpd6oCacTulkN3QRuAONo1qSXbLI'
access_token_secret = 'A6q3cgql3JQOdS05mDbOReuZ9EF3Q6ztbHRJAFGfMHy4v'

#Tweepy API methods to scrape searched Tweets
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#My weird text graphics lmao
print('-------------------------\n\nTwitter Sentiment Tool\n\nSentimental.ly\n\n-------------------------\n')
#What the user desires to search
stringtobesearched = input('What would you like to run the twitter sentiment analysis on?: ')

#Tweepy API method to search inputted string
public_tweets = api.search(stringtobesearched)

#Polarity and Subjectivity on input
polarityans = 0
subjectivityans = 0
count = 0
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    if (analysis.sentiment.subjectivity != 0 and analysis.sentiment.polarity != 0):
        subjectivityans += analysis.sentiment.subjectivity
        polarityans += analysis.sentiment.polarity
        count += 1
    print(analysis.sentiment)
print('-----------------------------------')
print('\nResults for '+ stringtobesearched +':\n \nPOLARITY: ' + str(polarityans/count) + "\nSUBJECTIVITY: " + str(subjectivityans/count) + '\n')
if((polarityans/count) > 0.1):
    print('\nPositive by: '+ str(polarityans/count) + '\n')
elif((polarityans/count) < 0.1):
    print('\nNegative by: '+ str(polarityans/count) + '\n')
else:
    print('\nNetrual' + '\n')
print('\n')