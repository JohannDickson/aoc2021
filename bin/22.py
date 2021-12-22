#! /usr/bin/env python3

import os


testfile = "../test/22_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.strip() for x in f.readlines()]

inputfile = "../input/22.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.strip() for x in f.readlines()]


def helper():
    return


def part1(numbers):
    return None


if __name__ == '__main__':
    test1 = part1(testInput)
    expected1 = None
    print(f"Test part 1 ({expected1}):", test1)
    if test1 == expected1:
        print("Part 1:", part1(myInput))
