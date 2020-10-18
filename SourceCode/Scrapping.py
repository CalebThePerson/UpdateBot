from bs4 import BeautifulSoup
import requests
import time
import datetime
import itertools as IT
from main import main as yeth


def Compare(ArrayOne, Arraytwo):
    for one, two in zip(ArrayOne,Arraytwo):
        if one != two:
            return one


while True:

    time.sleep(10)
    #The Url we are using
    url = "https://github.com/CalebThePerson?tab=repositories"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    #calling teh website then saving the html source
    response = requests.get(url, headers = headers)
    soup = BeautifulSoup(response.text, features="xml")

    #Goind throug all of the shit, and looking for repo names
    AllMyRepos = soup.find_all("a", itemprop = "name codeRepository")

    #Creating an array of repo names
    RepoArray = []
    for repo in AllMyRepos:
        RepoArray.append(repo.get_text())
        # print(repo.get_text())
        # print(repo.get("href"))

    #Creating an array of repo dates
    AllTheDates = soup.find_all(class_="no-wrap")
    DateArray = []

    for date in AllTheDates:
        originaldate = date.get("datetime")
        newdate = originaldate.replace("T", " ")
        newdate = newdate.replace("Z", "")
        TrueDate = datetime.datetime.strptime(newdate, '%Y-%m-%d %H:%M:%S')
        DateArray.append(TrueDate)

    WifiDict = {}
    for name, date in zip(RepoArray, DateArray):
        WifiDict[name] = date


    file = open("Poggers.html", "r").read()
    OnSiteSoup = BeautifulSoup(file, features = "xml")
    OnSiteRepo = OnSiteSoup.find_all("a", itemprop = "name codeRepository")

    OnSiteArray = []
    for repo in OnSiteRepo:
        # print(repo.get("href"))
        OnSiteArray.append(repo.get("href"))

    OnSiteDate = OnSiteSoup.find_all(class_="no-wrap")
    OnDateArray = []


    for date in OnSiteDate:        
        originaldate = date.get("datetime")
        newdate = originaldate.replace("T", " ")
        newdate = newdate.replace("Z", "")
        TrueDate = datetime.datetime.strptime(newdate, '%Y-%m-%d %H:%M:%S')
        OnDateArray.append(TrueDate)

    
    OnSiteDict = {}
    for name, date in zip(OnSiteArray, OnSiteDate):
        OnSiteDict[name] = date


    if RepoArray != OnSiteArray:
        print("Taddaaaaa")

    Difference = "daate"
    if DateArray != OnDateArray:
        Difference = Compare(DateArray, OnDateArray)

        try:
            with open("Poggers.html", mode="r+") as PoggersFile:
                PoggersFile.truncate(0)
                PoggersFile.write(str(soup))
                PoggersFile.close
        except FileExistsError:
            print("WElp damn")

if Difference != "daate":
    Name = list(WifiDict.keys())[list(WifiDict.values()).index(Difference)]
    yeth(Name)
    print(Name)
        
    

    

    











