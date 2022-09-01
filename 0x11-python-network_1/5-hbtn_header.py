#!/usr/bin/python3
"""script that takes in a URL sends a request to the URL and 
displays the value of the variable X-Request-Id"""
import requests
import sys

if __name__ == '__main__':
    """module to displays the value of the variable X-Request-Id"""
    
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
