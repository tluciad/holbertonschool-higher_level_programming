#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if not sentence:
        length = None
    else:
        first = sentence[0]
        tuple1 = (length, first)
    return tuple1
