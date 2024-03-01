#!/usr/bin/python3
"""
Python script that takes your Github credentials (username and password)
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    from requests.auth import HTTPBasicAuth
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    r = requests.get(url, auth=HTTPBasicAuth(argv[2], argv[3]))
    try:
        commits = r.json()
        for commit in commits[:10]:
            print(commit.get('sha'), end=': ')
            print(commit.get('commit').get('author').get('name'))
    except ValueError:
        print('Not a valid JSON')
