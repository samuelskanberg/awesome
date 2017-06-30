#!/usr/bin/env python3

"""
This is an awesome script
"""

import sys

"""
Will add two numbers
"""
def add(a, b):
    return a+b

"""
Will multiply two numbers
"""
def mul(a, b):
    return a*b

if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    total = add(a, b)
    print("Total: {}".format(total))
