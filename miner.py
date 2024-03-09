import os
from github import Github

# Authentication is defined via github.Auth
from github import Auth

# load GH_TOKEN environment variables
token = os.environ["GH_TOKEN"]
print(token)

# using an access token
auth = Auth.Token(token)

# Public Web Github
g = Github(auth=auth)

def get_pull_request(repo, number):
    repo = g.get_repo(repo)
    return repo.get_pull(number)

if __name__ == '__main__':
    # get tensorflow pull 63229
    pull = get_pull_request("tensorflow/tensorflow", 62199)
    commit=pull.get_commits()[0]
    print(commit)

    # print usage
    rate=g.get_rate_limit()
    print(rate.core)
    print(rate.graphql)

    # open tensorflow repository
    from git import Repo
    repo = Repo("~/tensorflow")
    print(repo)
    
    # get pull request commit and diff of the commit with its parent
    git_commit = repo.commit("20c20c2f3ec9e4d8ec5b0846c0b491b00132e664")
    print(git_commit)
    diff=git_commit.diff(git_commit.parents[0])
    print(diff)

    # To close connections after use
    g.close()
