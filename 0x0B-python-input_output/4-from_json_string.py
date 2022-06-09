#!/usr/bin/python3
"""unction that returns an object
(Python data structure) represented by
a JSON string"""
import json


def from_json_string(my_str):
    """Prototype of function"""
    return (json.loads(my_str))
