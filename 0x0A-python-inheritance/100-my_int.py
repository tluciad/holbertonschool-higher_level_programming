#!/usr/bin/python3
"""a class MyInt that inherits from int:"""


class MyInt(int):
    def __eq__(self, other):
        """compare equality"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """compare equality"""
        return not super().__ne__(other)
