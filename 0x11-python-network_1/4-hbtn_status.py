#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""
import requests
import sys

if __name__ == '__main__':
    """module to display like the example"""
    """Body response:$
    - type: <class 'str'>$
    - content: OK$"""
    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(r.text.__class__))
    print("\t- content: {}".format(r.text))
