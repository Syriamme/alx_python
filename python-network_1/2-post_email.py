#!/usr/bin/env python3
"""
This module takes in a URL and an email address, sends a POST request to the
URL with the email as a parameter (in the variable named 'email'), and prints
the body of the response.
"""

import requests
import sys

def send_post_request(url, email):
    """
    Sends a POST request to the specified URL with the given email address
    as a parameter, and prints the body of the response.
    
    Args:
        url (str): The URL to send the POST request to.
        email (str): The email address to be sent as a parameter.
    """
    data = {'email': email}
    response = requests.post(url, data=data)
    print(response.text)

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
