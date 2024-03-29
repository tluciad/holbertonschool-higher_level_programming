#!/usr/bin/python3
"""Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter."""
import requests
import sys
if __name__ == '__main__':
    """module to displays display the id and
    name like this: [<id>] <name>"""
    letter = {'q': ""}
    try:
        letter['q'] = sys.argv[1]

    except Exception:
        pass
    r = requests.post('http://0.0.0.0:5000/search_user', letter)
    try:
        jsonLet = r.json()
        if len(jsonLet.keys()) > 0:
            print("[{}] {}".format(jsonLet.get('id'), jsonLet.get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
