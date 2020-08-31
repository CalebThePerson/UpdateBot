import requests

class GitHubApi():
    #The urls we will be using throughout the code

    def init(self):
        self.url = "https://api.github.com"
        self.MyUrl = "https://api.github.com/repos/CalebThePerson/DoujinshiFinder"
        self.CommitURL = "https://api.github.com/repos/CalebThePerson/DoujinshiFinder/commits"

        #Calls the GitHub api and then calls specific information
    def CommitInfo(self):
        request = requests.get(url=self.CommitURL)
        data = request.json()

        CommitMessage = data[0]["commit"]["message"]
        NumberOfCommits = 0

        for commits in range(0,len(data)):
            NumberOfCommits += 1
        
        return CommitMessage, NumberOfCommits

    def Checker(self):
        #Think of way to check and tell that the commit is new and haven't already been tweeted about
        '''
        So what we can do is filter through my tweets and then we can have it filter through it for the commit number
        '''
        pass



yeth = GitHubApi()
