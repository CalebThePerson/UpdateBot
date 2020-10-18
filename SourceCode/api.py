from Tokens import ConsumerSecret,ConsumerKey,AccessToken,SecretToken, GitHubClient, ClientSecret
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

    def __init__(self, name):
        self.reponame = name
        self.TheCommit = 0
        self.MEssage = ""
        self.ThirdVariable = ""
        self.TheTweet = ""
        
    def TweetingUpdate(self):
        self.CommitNumber()
        if self.TheTweet.strip():
            api.update_status(f"{self.TheTweet}")
        print("Done")

    def FilterForRepo(self, Tweet):
        if self.reponame in Tweet:
            return Tweet
        else:
            pass


    def CommitNumber(self):
        welp = []

        for status in LimitHandler(tweepy.Cursor(api.user_timeline).items(30)):
            welp.append(str(status.text))
        
        FilteredRepoArray = []
        for tweet in welp:
            if self.FilterForRepo(tweet) != None:
                FilteredRepoArray.append(self.FilterForRepo(tweet))
        
        print(FilteredRepoArray)

        NumerArray = []
        for tweet in FilteredRepoArray:
            for character in range(0,len(tweet)):
                try:
                    int(tweet[character])

                    if int(tweet[character]):
                        NumerArray.append(int(tweet[character: character+2]))
                    else:
                        NumerArray.append(int(tweet[character]))

                except ValueError:
                    pass
                    
        print(NumerArray)

        if NumerArray == []:
            NumerArray.append(0)

        self.GatherInfo(max(NumerArray))


    

    def GatherInfo(self, LastNumber):
        BitBub = GitHubApi(self.reponame)
        print(LastNumber)
        if LastNumber == 0:
            if BitBub.CommitInfo(999) !=False:
                
                self.Message, self.TheCommit = BitBub.CommitInfo(999)
                self.TheTweet = f"{self.reponame}, Commit#{self.TheCommit} : {self.Message}. {BitBub.URLwithnoAPI}"
            else:
                pass
        else:

            SearchingFor = 1 + LastNumber

            if BitBub.CommitInfo(SearchingFor) != False:
                self.Message, self.TheCommit = BitBub.CommitInfo(SearchingFor)
                self.TheTweet = f"{self.reponame}, Commit#{self.TheCommit} : {self.Message}. {BitBub.URLwithnoAPI}"

            
            elif BitBub.CommitInfo(SearchingFor) == False:
                print("This  has already beeen published")

    

    def BotherMakar(self):
        api.send_direct_message("958734505006608384", "Hey cutie")
        print("Done")

                


# yeth = TweetBot(name="UpdateBot")
# # yeth.CommitNumber()
# # yeth.BotherMakar()
# yeth.TweetingUpdate()