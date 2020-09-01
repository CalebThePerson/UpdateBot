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
        api.update_status("Pleae Help Me")
        print("Done")

    def Stuff(self,TheNum):
        #This functions double checks to make sure that the shit is actually a number
        try:
            if int(TheNum):
                print("Good")
                return TheNum

        except ValueError:
            print("Not poggers")
            pass

            

    def MaxCommitNumber(self):
        pass
        # return NewArrayForChecking[0]
            
    def HereWeGoAgain(self, TheStats, meth):
        #This is for single digit tweets
        if len(meth) < 10 and len(meth) <= 9:
            print(TheStats)
            return TheStats[8:9]

            #Double Digit Tweets
        elif len(meth) > 9 and len(meth) <= 10:
            print(TheStats)
            return TheStats[8:10]

            #The rest because im too lazy to do this
        else:
            print("Not poggers")
            pass
            

    def FilterFunction(self, TheTweet):
        if filter(TheTweet, "Commit #"):
            return TheTweet
        else:
            return
        

    def CommitNumber(self):
        welp = []
        
        #Gets the certain number of tweets from my personal timeline
        for status in LimitHandler(tweepy.Cursor(api.user_timeline).items(7)):
            #Adds the tweets to an array
            x = str(status.text)
            welp.append(x)
        
        #Creates new array and then filters the tweets that has the word Commit in it
        NewArray = []
        for num in range(0,len(welp)):
            if self.FilterFunction(welp[num]) != None:
                kerchew = self.FilterFunction(welp[num])
                NewArray.append(kerchew)


        
        LengthofNewArray = len(NewArray)
        CommitArray = []

        #Loops through the array and the gets the commit number from the tweets
        for num in range(0,LengthofNewArray):

            TheThing = NewArray[num]
            yeth = [i for ele in NewArray[num] for i in ele]
            print(yeth)
            print(len(yeth))
            HopefullyTheCommitTweet = self.HereWeGoAgain(TheThing,yeth)
            
            if HopefullyTheCommitTweet != None:
                CommitArray.append(HopefullyTheCommitTweet)
            else:
                pass
        
        print(CommitArray)

        #Now we are just double checking to make sure that the things in the array are actually numbers and no stupid bug

        for num in range(0, len(CommitArray)):
            self.Stuff(CommitArray[num])





    def BotherMakar(self):
        api.send_direct_message("958734505006608384", "Hey cutie")
        print("Done")


yeth = TweetBot()
# yeth.TweetingUpdate()
yeth.CommitNumber()
# yeth.BotherMakar()