#!/usr/bin/python3
'''test the classes'''
import unittest
import datetime
import sys
sys.path.append("/alx-higher_level_programming/BnB")
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    '''Test the base class methods and attributes'''
    @classmethod
    def setUpClass(cls):
        cls.obj = BaseModel()

    def test_uuid(self):
        '''test the uuid'''
        self.assertIsInstance(TestBase.obj, BaseModel)
        self.assertTrue(TestBase.obj.id)

    def test_datetime(self):
        self.assertIsInstance(TestBase.obj.created_at, datetime.datetime)
        self.assertIsInstance(TestBase.obj.updated_at, datetime.datetime)
        TestCase.

    @classmethod
    def tearDownClass(cls):
        del cls.obj

if __name__ == "__main__":
    unittest.main()
