#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as exception:
        import sys
        print("Exception: {}".format(exception), file=sys.stderr)
        return False
