#!/usr/bin/python3
"""Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id"""
import requests
import sys

if __name__ == '__main__':
    """use Basic Authentication with a personal access
    token as password to access to your information """
    user = sys.argv[1]
    password = sys.argv[2]

    r = requests.get('https://api.github.com/user', auth=(user, password))
    try:
        print(r.json().get('id'))
    except Exception:
        print('None')
