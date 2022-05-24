#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as exception:
        import sys
        print("Exception: {}".format(exception), file=sys.stderr)
        return None
