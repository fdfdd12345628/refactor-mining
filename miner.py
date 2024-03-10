import os
from github import Github
import difflib


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
    # pull = get_pull_request("tensorflow/tensorflow", 62199)
    # commit=pull.get_commits()[0]
    # print(commit)

    # print usage
    rate=g.get_rate_limit()
    print(rate.core)
    print(rate.graphql)

    # open tensorflow repository
    from git import Repo
    repo = Repo("~/tensorflow")
    print(repo)
    
    # get pull request commit and diff of the commit with its parent
    git_commit = repo.commit("6f64ad5d767a034df45a5eaab8b36fd688cd1217")
    print(git_commit)
    diff=git_commit.diff(git_commit.parents[0])
    single_diff=diff[0]
    d = difflib.Differ()
    diff = d.compare(single_diff.a_blob.data_stream.read().decode().splitlines(), single_diff.b_blob.data_stream.read().decode().splitlines())
    print('\n'.join(diff))

    # To close connections after use
    g.close()
