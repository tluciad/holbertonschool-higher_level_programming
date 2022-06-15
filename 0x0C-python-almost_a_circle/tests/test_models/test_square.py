#!/usr/bin/python3
""""Unittest for class Square"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_SquareModels(unittest.TestCase):
    """testing Square model"""

    def testSquareModel1(self):
        test_sq = Square(1)
        self.assertEqual(test_sq.width, 1)
        self.assertEqual(test_sq.height, 1)
        self.assertEqual(test_sq.size, 1)
    
    def test_square_area(self):
        test_square = Square(3)
        self.assertEqual(test_square.area(), 9)



if __name__ == '__main__':
    unittest.main()
