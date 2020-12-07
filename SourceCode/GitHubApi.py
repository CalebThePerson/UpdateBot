import requests
from Tokens import GitHubClient, ClientSecret


#The urls we will be using throughout the code

class GitHubApi():

    def __init__(self, reponame):
        self.url = "https://api.github.com"
        self.MyUrl = f"https://api.github.com/repos/CalebThePerson/{reponame}"
        self.CommitURL = f"https://api.github.com/repos/CalebThePerson/{reponame}/commits"
        self.URLwithnoAPI = f"https://github.com/CalebThePerson/{reponame}"


    
    def Checker(self, CommitNumber, CommitWeWant):
        #Confirms taht this is a new tweet and the tweet we want
        if CommitNumber == CommitWeWant:
            return True
        else: 
            return False


        #Calls the GitHub api and then calls specific information
    def CommitInfo(self, CommitWeWant):
        request = requests.get(url=self.CommitURL)
        data = request.json()

        print(self.CommitURL)
        CommitMessage = data[0]["commit"]["message"]
        NumberOfCommits = 0

        for commits in range(0,len(data)):
            NumberOfCommits += 1

        print(CommitMessage, NumberOfCommits)

        if self.Checker(CommitWeWant,NumberOfCommits) == True:
            print(CommitWeWant)
            print(NumberOfCommits)
            return CommitMessage, NumberOfCommits
        else:
            if CommitWeWant == 999:
                print(NumberOfCommits, CommitWeWant)
                return CommitMessage, NumberOfCommits
            else:
                return False


    def GatherInfo(self, CommitWeWant):
        request = requests.get(url=self.CommitURL)
        data = request.json()

        CommitMessage = data[int(CommitWeWant)]["commit"]["message"]

        NumberOfCommits = 0
        for commits in range(0,len(data)):
            NumberOfCommits+=1 

        return CommitMessage, NumberOfCommits




