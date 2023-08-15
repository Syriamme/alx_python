#!/usr/bin/env python3
"""
This module takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter in the variable named 'q'. It then prints the response
based on the specified conditions.
"""

import requests
import sys

def search_user(letter):
    """
    Sends a POST request to the specified URL with the given letter as a parameter,
    and prints the response based on the conditions described.

    Args:
        letter (str): The letter to be sent as a parameter.
    """
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': letter}
    response = requests.post(url, data=data)

    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    search_user(letter)
