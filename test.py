#!/usr/bin/env python3

import unittest

from awesome import add

class AwesomeTest(unittest.TestCase):
    def test_add(self):
        total = add(1, 2)
        self.assertEqual(3, total)


if __name__ == "__main__":
    unittest.main()
