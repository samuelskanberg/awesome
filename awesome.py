#!/usr/bin/env python3

import sys

def add(a, b):
    return a+b

def mul(a, b):
    return a*b

if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    total = add(a, b)
    print("Total: {}".format(total))
