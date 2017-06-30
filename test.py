#!/usr/bin/env python3

import unittest

from awesome import add, mul, sub

class AwesomeTest(unittest.TestCase):
    def test_add(self):
        total = add(1, 2)
        self.assertEqual(3, total)
    def test_mul(self):
        total = mul(2, 3)
        self.assertEqual(6, total)
    def test_sub(self):
        total = sub(4, 2)
        self.assertEqual(2, total)

if __name__ == "__main__":
    unittest.main()
