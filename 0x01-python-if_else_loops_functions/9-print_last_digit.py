#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        lastdigit = abs(number) % 10
    elif number < 0:
        lastdigit = abs(number) % 10
    print(f"{lastdigit}", end='')
    return(lastdigit)
