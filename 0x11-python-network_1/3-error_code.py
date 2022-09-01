#!/usr/bin/python3
""""script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter and displays the
body of the response (decoded in utf-8)"""
if __name__ == '__main__':
    """module to displays the value of the X-Request-Id"""
    import urllib.request
    import urllib.parse
    from urllib.error import HTTPError, URLError
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('UTF-8'))

    except urllib.error.HTTPError as error:
        print('Error code: {}'.format(error.code))
