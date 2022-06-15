#!/usr/bin/python3
""""Unittest for class Base"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_BaseModels(unittest.TestCase):
    """testing base class"""

    def test_id(self):
        b_1 = Base()
        b_2 = Base(2)
        b_3 = Base(8)
        self.assertEqual(b_1.id, 1)
        self.assertEqual(b_2.id, 2)
        self.assertEqual(b_3.id, 8)

    def Set_up(self):
        Base.__nb_objects = 0

    def testStrid(self):
        bs = Base('1')
        self.assertEqual(bs.id, '1')

   

if __name__ == '__main__':
    unittest.main()
