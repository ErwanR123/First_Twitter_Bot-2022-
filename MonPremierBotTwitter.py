import tweepy

auth= tweepy.OAuth1UserHandler("CDT35viLI82xFnP9UF84WSpFA","IDjMi9y53x1DkTh48zHQ3bCsH0gHwGxlQUUz9EhTdctpr8UK5X")
auth.set_access_token("1532767669996425216-0lRkSLNJzgXXWXiyuMXS3TV08v07vB","9uLWmHifE5A3pinZf87z40C0E4mqcAjxmfuqYcX7hFOAS")

api = tweepy.API(auth)
try:
    api.verify_credentials()
    print("ok")
except:
    print("Erreur de connection")