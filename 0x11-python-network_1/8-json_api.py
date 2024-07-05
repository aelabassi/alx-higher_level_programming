#!/usr/bin/python3
"""Module that sends a POST request with a letter as a parameter"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={'q': q})
    try:
        response = response.json()
        if response:
            print("[{}] {}".format(response.get('id'), response.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
