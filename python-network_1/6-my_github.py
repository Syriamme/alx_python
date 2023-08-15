#!/usr/bin/env python3
"""
This module takes a GitHub username and personal access token as arguments, and
uses the GitHub API to display the user's ID. Basic Authentication is used with
the personal access token as the password.
"""

import requests
import sys

def fetch_github_id(username, token):
    """
    Uses the GitHub API to fetch and print the user's ID, using Basic Authentication.

    Args:
        username (str): The GitHub username.
        token (str): The personal access token for authentication.
    """
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        print(response.json()['id'])
    else:
        print("Error fetching user ID:", response.status_code)

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    fetch_github_id(username, token)
