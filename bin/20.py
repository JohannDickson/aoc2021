#! /usr/bin/env python3

import os
import json
from math import ceil, floor


testfile = "../test/20_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.strip() for x in f.readlines()]

inputfile = "../input/20.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.strip() for x in f.readlines()]


def find_deepest(numbers):
    return None


def part1(numbers):
    result = 0
    for i in numbers:
        print(json.loads(i))
        reduce(json.loads(i))
    return result


if __name__ == '__main__':
    expected1 = None
    test1 = part1(testInput)
    print("Test 1:", expected1, expected1==test1, test1)
    if expected1 == test1:
        print("Part 1:", part1(myInput))
