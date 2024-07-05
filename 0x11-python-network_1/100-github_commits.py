#!/usr/bin/python3
"""" script that list the 10 recent commits of a repository """
import requests
import sys

if __name__ == "__main__":
    url = ('https://api.github.com/repos/{}/{}/commits'
           .format(sys.argv[2], sys.argv[1]))
    response = requests.get(url)
    commits = response.json()
    for commit in commits[:10]:
        print("{}: {}".format(commit.get('sha'),
                              commit.get('commit').get('author').get('name')))
