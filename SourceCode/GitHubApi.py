import requests

class GitHubApi():
    url = "https://api.github.com"
    MyUrl = "https://api.github.com/repos/CalebThePerson/DoujinshiFinder"

    def CommitInfo(self):
        CommitURL = "https://api.github.com/repos/CalebThePerson/DoujinshiFinder/commits"
        request = requests.get(url=CommitURL)
        data = request.json()

        CommitMessage = data[0]["commit"]["message"]
        NumberOfCommits = 0

        for commits in range(0,len(data)):
            NumberOfCommits += 1
        
        return CommitMessage, NumberOfCommits



yeth = GitHubApi()
yeth.CommitInfo()