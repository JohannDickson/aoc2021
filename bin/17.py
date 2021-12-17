#! /usr/bin/env python3

import os
import re


testfile = "../test/17_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = f.read().strip()

inputfile = "../input/17.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = f.read().strip()


def part1(trickshot):
    print(trickshot)
    reg = re.compile("target area: x=(\d+)\.\.(\d+), y=(\-\d+)\.\.(\-\d+)")
    [res] = re.findall(reg, trickshot)
    (xmin,xmax,ymin,ymax) = [int(x) for x in res]
    return None


if __name__ == '__main__':
    test1 = part1(testInput)
    expected1 = 45
    if test1 == expected1:
        print("Part 1:", part1(myInput))
