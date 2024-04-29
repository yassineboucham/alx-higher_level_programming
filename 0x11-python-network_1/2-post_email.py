#!/usr/bin/python3
"""
    a Python script that takes in a URL and an email,
    sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}
    try:
        if url and email:
            encoding = urllib.parse.urlencode(data).encode('utf-8')
            requet = urllib.request.Request(url, data=encoding, method='POST')
            with urllib.request.urlopen(requet) as res:
                respons = res.read().decode('utf-8')
            print(respons)
    except Exception as e:
        print("error: {}".format(e))
