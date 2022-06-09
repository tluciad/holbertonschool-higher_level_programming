#!/usr/bin/python3
"""a class MyInt that inherits from int:"""

class MyInt(int):
    def __eq__(self, __o: object) -> bool:
        """compare equality"""
        return not super().__eq__(__o)

    def __ne__(self, __o: object) -> bool:
        """compare equality"""
        return not super().__ne__(__o)
        