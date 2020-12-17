import tweepy
import requests
import json

#authenticates to twitter and returns
auth = tweepy.OAuthHandler("LwFDQXqYKFAztmz5uaNi1kQbO","RFw4LYweYXFxFRJjREX8wU27BLMwm0TtRduclM8nlK6n4PI2fa")
auth.set_access_token("1339319976960864260-1aDLh9VEiZvW3TQr3jsIiwztubmCvd","oF3Knos3IDkP94w7a1ZS7vetLm8t0wOwWh47GVUqDn9EP")

api = tweepy.API(auth)

#makes sure authentication is successfull
try:
    api.verify_credentials()
    print("Authentication successful")
except:
    print("Error during authentication")

#API get call
def try_quote():
    
    response = requests.get("http://api.forismatic.com/api/1.0/get?method=getQuote&format=json&lang=en")
    json_dict = response.json()
    
    quote = []
    quote.append(json_dict["quoteText"])
    quote.append(json_dict["quoteAuthor"])
    return quote

#attempts to grab a quote from forismatic.com API
#the API seems to randomly add "\" characters which need to be escaped so...
#the function just keeps trying until it works lol 
#bESt PraCTiCeS
def get_quote():
    try:
        return try_quote()
    except:
        get_quote()

quote = get_quote()

last = quote[0][len(quote[0])-1:]
if(last == " "):
    quote[0] = quote[0][:len(quote[0])-1]

#tweets the tweet
def tweet(quote):
    try:
        api.update_status("do your homework." + '\n\n"' + quote[0] + '"' + " -" + quote[1])
        print("Success")
    except:
        print("Tweet attempt unsuccessful")

tweet(quote)
