#!/usr/bin/python3

"""
Testing the base"""
import unittest
import sys
sys.path.append("../models")
Base = __import__('base').Base


class BaseTest(unittest.TestCase):
    """Test class"""
    def test_id(self):
        """test id function"""
        b1 = Base(22)
        b2 = Base()
        b3 = Base(33)
        b4 = Base()
        self.assertEqual(b1.id, 22)
        self.assertEqual(b2.id, 1)
        self.assertEqual(b3.id, 33)
        self.assertEqual(b4.id, 2)

if __name__ == "__main__":
    unittest.main()
