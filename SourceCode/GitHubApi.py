import requests

#The urls we will be using throughout the code
url = "https://api.github.com"
MyUrl = "https://api.github.com/repos/CalebThePerson/DoujinshiFinder"
CommitURL = "https://api.github.com/repos/CalebThePerson/DoujinshiFinder/commits"
URlWithNoAPI = "https://github.com/CalebThePerson/DoujinshiFinder"

class GitHubApi():
    
    def Checker(self, CommitNumber, CommitWeWant):
        #Confirms taht this is a new tweet and the tweet we want
        if CommitNumber == CommitWeWant:
            return True
        else: 
            return False


        #Calls the GitHub api and then calls specific information
    def CommitInfo(self, CommitWeWant):
        request = requests.get(url=CommitURL)
        data = request.json()

        CommitMessage = data[0]["commit"]["message"]
        NumberOfCommits = 0

        for commits in range(0,len(data)):
            NumberOfCommits += 1

        print(CommitMessage, NumberOfCommits)

        if self.Checker(CommitWeWant,NumberOfCommits) == True:
            return CommitMessage, NumberOfCommits
        else:
            return False


