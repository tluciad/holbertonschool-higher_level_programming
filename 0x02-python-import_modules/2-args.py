#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    print("{}".format(len(argv) - 1), end=" ")
    if len(argv) - 1 == 0:
        print("arguments.")
    elif len(argv) - 1 == 1:
        print("argument:")
    else:
        print("arguments:")
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
