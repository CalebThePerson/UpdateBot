from Tokens import ConsumerSecret,ConsumerKey,AccessToken,SecretToken
from GitHubApi import GitHubApi
import tweepy
import time

auth = tweepy.OAuthHandler(ConsumerKey,ConsumerSecret)
auth.set_access_token(AccessToken,SecretToken)
api = tweepy.API(auth)

class AnotherTwitterAPI():
    def __init__(self, name, Number , RealNumber):
        self.reponame = name
        self.TheCommit = Number
        self.TheReal = RealNumber
        self.Message = ""
        self.ThirdVariable = ""
        self.TheTweet = ""

    def TweetingUpdate(self):
        api.update_status(f"{self.TheTweet}")
        print("Done")

    def GettingTheInfo(self):
        BitBub = GitHubApi(self.reponame)
        self.Message, Number = BitBub.GatherInfo(self.TheCommit)
        self.TheTweet = self.TheTweet = f"{self.reponame}, Commit#{self.TheReal} : {self.Message}. {BitBub.URLwithnoAPI}"
        print(self.TheTweet)

        self.TweetingUpdate()