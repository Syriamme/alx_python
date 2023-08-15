#!/usr/bin/env python3
"""
-The module will takes the GitHub username
and personal access token
-Uses the GitHub API
"""

import requests
import sys

def fetch_github_id(username, token):
    """
    -Fetching and printing the GitHub 
    user's ID using Basic Authentication

    Args:
        Username (str): gitHub username
        Token (str): personal access token
    """
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        print(response.json().get('id'))

    else:
        print("None")

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    fetch_github_id(username, token)
