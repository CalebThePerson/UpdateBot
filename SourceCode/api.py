from Tokens import ConsumerSecret,ConsumerKey,AccessToken,SecretToken
import tweepy

class TweetBot():
    auth = tweepy.OAuthHandler(ConsumerKey,ConsumerSecret)
    auth.set_access_token(AccessToken,SecretToken)
    api = tweepy.API(auth)

    def TweetingUpdate():
        pass

