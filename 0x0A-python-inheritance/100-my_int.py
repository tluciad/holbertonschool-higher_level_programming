#!/usr/bin/python3
"""a class MyInt that inherits from int:"""


class MyInt(int):
    """inherits from int"""

    def __eq__(self, __o: object) -> bool:
        """compare equality"""
        return super().__ne__(__o)

    def __ne__(self, __o: object) -> bool:
        """compare equality"""
        return super().__eq__(__o)
