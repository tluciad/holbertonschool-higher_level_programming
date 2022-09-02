#!/usr/bin/python3
"""Python script that takes in a URL, sends a request
to the URL and displays the body of the response"""
import requests
import sys

if __name__ == '__main__':
    """module to displays the value of the variable X-Request-Id"""

    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print('Error code: {}'.format(r.status_code))
    else:
        print(r.text)
