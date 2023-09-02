#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Tests the return value of max_integer
    """
    def test_max_integer(self):
        self.assertEqual(max_integer([35, 88, 4, 900, 1, 20]), 900)
        self.assertEqual(max_integer([]), None)


if __name__ == "__main__":
    unittest.main()
