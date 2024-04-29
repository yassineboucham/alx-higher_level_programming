#!/usr/bin/python3
"""
 Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


fetch = requests.get("https://alx-intranet.hbtn.io/status")
content = fetch.text
print("Body response:")
print("\t- type: {}".format(type(content)))
print("\t- content: {}".format(content))
