#!/usr/bin/env python3
"""
-The module will  takes in a URL, sends a request to the URL
-It will send a POST request to the URL with the email as a parameter
-Will display the body of the response.
"""


import requests
import sys

def send_post_request(url, email):
    """
    -Takes in a URL, sends a request to the URL
    -Will display the body of the response.
    
    -Args:
        url: The URL
        email: The email address
    """
    data = {'email': email}
    response = requests.post(url, data=data)
    print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    
    send_post_request(url, email)
