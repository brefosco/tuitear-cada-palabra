import time
import tweepy
from secret import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
print("logged in")

me = api.me()
file = open("palabras.txt", "r", encoding="utf-8")
f = file.readlines()
file.close()
ultima_palabra = ''

for line in f:
    print("intentando imprimir {}".format(line))
    try:
        api.update_status(line)
        ultima_palabra = line

        print("tweeted " + line)
        time.sleep(600)

    except Exception as e:
        print("exception {}".format(e))

print("TERMINADO")
api.update_status('ya no hay nada para tuitear')
