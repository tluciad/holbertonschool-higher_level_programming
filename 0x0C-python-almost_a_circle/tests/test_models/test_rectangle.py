#!/usr/bin/python3
""""Unittest for class Base"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_RectangleModels(unittest.TestCase):
    """testing Rectangle  model"""

    def testRectangle1(self):
        RectangleA = Rectangle(3, 5)
        self.assertEqual(RectangleA.width, 3)
        self.assertEqual(RectangleA.height, 5)
           
    def testRectangle2(self):
        RectangleB = Rectangle(3, 5, 8)
        self.assertEqual(RectangleB.width, 3)
        self.assertEqual(RectangleB.height, 5)
        self.assertEqual(RectangleB.x, 8)

    def testRectangle3(self):
        RectangleC = Rectangle(3, 5, 8, 2)
        self.assertEqual(RectangleC.width, 3)
        self.assertEqual(RectangleC.height, 5)
        self.assertEqual(RectangleC.x, 8)
        self.assertEqual(RectangleC.y, 2)

    def testRectangle4(self):
        RectangleD = Rectangle(3, 5, 8, 2, 6)
        self.assertEqual(RectangleD.width, 3)
        self.assertEqual(RectangleD.height, 5)
        self.assertEqual(RectangleD.x, 8)
        self.assertEqual(RectangleD.y, 2)
        self.assertEqual(RectangleD.id, 6)

    def testRectangleArea(self):
        RectangleE = Rectangle(8, 3)
        self.assertEqual(RectangleE.area(), 24)

if __name__ == '__main__':
    unittest.main()
