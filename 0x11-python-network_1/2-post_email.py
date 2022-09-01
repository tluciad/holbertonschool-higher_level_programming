#!/usr/bin/python3
""""script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter and displays the
body of the response (decoded in utf-8)"""
if __name__ == '__main__':
    """module to displays the value of the X-Request-Id"""
    import urllib.request
    import urllib.parse
    import sys

    mail = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(mail).encode('utf-8')
    req = urllib.request.Request((sys.argv[1]), data)

    with urllib.request.urlopen(req) as response:
        print(response.read().decode('UTF-8'))
