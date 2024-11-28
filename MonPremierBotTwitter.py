import tweepy

auth= tweepy.OAuth1UserHandler("put_code","put_code")
auth.set_access_token("access_token","access_token")

api = tweepy.API(auth)
try:
    api.verify_credentials()
    print("ok")
except:
    print("Erreur de connection")
