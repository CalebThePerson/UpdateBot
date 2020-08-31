from Tokens import ConsumerSecret,ConsumerKey,AccessToken,SecretToken
from GitHubApi import GitHubApi
import tweepy
import time

auth = tweepy.OAuthHandler(ConsumerKey,ConsumerSecret)
auth.set_access_token(AccessToken,SecretToken)
api = tweepy.API(auth)

def LimitHandler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
            #pausing the funciton for 1000 ms if we hit the limt
        time.sleep(300)
    except RuntimeError:
        print("welp FUCk")
    except StopIteration:
        return

class TweetBot():

    def TweetingUpdate(self):
        api.update_status("Commit #7")
        pass


    def CommitNumber(self):
        for status in LimitHandler(tweepy.Cursor(api.user_timeline).items(2)):
            x = status.text
            pass

    def BotherMakar(self):
        api.send_direct_message("958734505006608384", "Hey cutie")


yeth = TweetBot()
yeth.CommitNumber()