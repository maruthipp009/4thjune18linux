#!/usr/bin/python3
import  tweepy
from textblob  import TextBlob
#  to connect with API 
consumer_key=""
consumer_sec=""
#  to get token 
access_token=""
access_secret=""
#  sending  consumer key and secret for check 
check=tweepy.OAuthHandler(consumer_key,consumer_sec)
#  NOW setting get_tokens
#print(dir(check))
check.set_access_token(access_token,access_secret)
#  by using  check we can connect to search api 
connected=tweepy.API(check)
#  now searching 
output=connected.search('Trumph')

# extracting  text words  

for i in  output:
    sample=i.text
    blob_data=TextBlob(sample)
    print(blob_data.sentiment)

