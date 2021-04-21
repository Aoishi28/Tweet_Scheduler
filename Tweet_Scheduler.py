import tweepy
import schedule
import time
from random import randint

from bs4 import BeautifulSoup
import requests
quotes=[]

#Extracting quotes to post on Twitter
url = 'https://blog.hubspot.com/sales/famous-quotes'
req = requests.get(url)
soup = BeautifulSoup(req.content, 'lxml')
reg=soup.findAll('div',{"class":'hsg-featured-snippet'})
for i in reg:
    q=i.findAll('li')
    for j in q:
        quotes.append(j.text)

print(quotes)

# Authenticate to Twitter

auth = tweepy.OAuthHandler("", "") #API Key. API secret key
auth.set_access_token("", "") #Access, Access secret

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

def send_message():
    auth = tweepy.OAuthHandler('','') #API Key. API secret key
    auth.set_access_token('','')#Access, Access secret
    api = tweepy.API(auth)

    num=randint(1,len(quotes)) #Choose a quote randomly since we can't post duplicate status on tweepy
    tweet = quotes[num]

    api.update_status(status=tweet)
    print('Tweeted: %s' % tweet)

schedule.every(2).minutes.do(send_message) # Schedule a new periodic job

while True:
    schedule.run_pending() # Check whether a scheduled task is pending to run or not
    time.sleep(1)


    