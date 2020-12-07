from PoggerAPI import AnotherTwitterAPI

def main():
    RepoName = input("Enter the Repo Name:")
    Number = input("Enter the commit you want , where 0 is the newest and the last number being the first one:")
    Real = input("Enter the Real Number:")
    AnotherBot = AnotherTwitterAPI(RepoName, Number, Real)
    AnotherBot.GettingTheInfo()

if __name__ == "__main__":
    main()