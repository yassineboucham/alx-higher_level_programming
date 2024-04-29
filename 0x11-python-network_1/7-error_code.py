#!/usr/bin/python3
"""
 a Python script that takes in a URL,
 sends a request to the URL and displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    if url:
        req = requests.get()
        if req.status_code != 200:
            print("Error code: {}".format(req.status_code))
        else:
            value = req.text()
            print(value)
