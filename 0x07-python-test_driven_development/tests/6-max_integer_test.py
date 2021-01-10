#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """class that to test maxInteger"""

    def test_types(self):
        """Test for types of variables"""
        self.assertRaises(TypeError, max_integer, [1, 2, 3, "hola"])
        self.assertRaises(TypeError, max_integer, ["hola"], ["n"])

    def test_equal(self):
        """Test for known results"""
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)
        self.assertEqual(max_integer([123, 565, 3, -5647]), 565)
        self.assertEqual(max_integer([-12, -23, -756, -2]), -2)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([0]), 0)

    def test_empty(self):
        """test empty variables"""
        empty_list = []
        self.assertIsNone(max_integer(empty_list))
        self.assertIsNone(max_integer())
        self.assertRaises(TypeError, max_integer, None)

if __name__ == "__main__":
    unittest.main()
