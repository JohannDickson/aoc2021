#! /usr/bin/env python3

import os
from collections import Counter


testfile = "../test/06_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [int(x) for x in f.read().strip().split(',')]

inputfile = "../input/06.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [int(x) for x in f.read().strip().split(',')]


def growfish(school):
    newFish = school[0]
    for i in range(1,9):
        school[i-1] = school[i]
    school[8] = newFish
    school[6] += newFish
    return school


def part1(lampfish, days):
    lampfish = Counter(lampfish)
    for i in range(0, days):
        lampfish = growfish(lampfish)
    return sum(lampfish.values())


if __name__ == '__main__':
    print("Part 1:", part1(myInput, 80))
    print("Part 2:", part1(myInput, 256))
