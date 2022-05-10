#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]
    tuple1 = (length, first)
    if not sentence:
        length = None
    else:
        return tuple1
