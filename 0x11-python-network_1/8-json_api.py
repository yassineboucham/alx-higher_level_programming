#!/usr/bin/python3
"""
 Python script that takes in a letter and sends a POST
 request to http://0.0.0.0:5000/search_user
 with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    q = sys.argv[1]
    if not q:
        q = ""
    data = {"q": q}
    res = requests.post("http://0.0.0.0:5000/search_user", data)
    try:
        value = res.json()
        if not value:
            print("No result")
        else:
            id = value.get('id')
            name = value.get('name')
            print("[{}] {}".format(id, name))
    except ValueError as v:
        print("Not a valid JSON")
