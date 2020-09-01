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

    def Stuff(self,TheArray):
        amount = len(TheArray)
        NewArrayForChecking = []

        for num in range(0,amount):

            try:
                if int(TheArray[num]):
                    print("Good")
                    print(TheArray[num])
                    NewArrayForChecking.append(TheArray[num])

            except ValueError:
                print("Not poggers")
                pass

            pass
        
        NewArrayForChecking.sort()
        # return NewArrayForChecking[0]
            

    def CharacterStruffRenameLater(self, TheStatus, yeth):
        if len(TheStatus) > 8 and len(yeth) < 9:
            print(TheStatus)
            return TheStatus[:8]
            
        elif len(TheStatus) > 9 and len(yeth) < 10:
            print(TheStatus)
            return TheStatus[:9]
            

    def FilterFunction(self, TheTweet):
        if filter(TheTweet, "Commit"):
            return TheTweet
        

    def CommitNumber(self):
        welp = []


        for status in LimitHandler(tweepy.Cursor(api.user_timeline).items(7)):


            x = str(status.text)
            print(x)[:8]
            
            if filter(x,"Commit #"):

                yeths = [i for ele in x for i in ele]
                welp.append(self.CharacterStruffRenameLater(x, yeths))

        print(welp)


                # print(status.text)

            # self.Stuff(welp)


    def BotherMakar(self):
        api.send_direct_message("958734505006608384", "Hey cutie")


yeth = TweetBot()
# yeth.TweetingUpdate()
yeth.CommitNumber()