#! /usr/bin/env python3

import os
from collections import Counter


testfile = "../test/14_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = f.read()

inputfile = "../input/14.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = f.read()


def part1(polymers, iterations):
    [poly, rules] = polymers.strip().split('\n\n')
    for _ in range(iterations):
        inserts = {}

        for r in rules.split('\n'):
            pair, new = r.split(' -> ')
            index = 0
            for j in range(poly.count(pair)):
                index = poly.index(pair, index)+1
                inserts[index] = new

        for i in sorted(inserts.keys(), reverse=True):
            poly = poly[:i] + inserts[i] + poly[i:]

    c = Counter(poly)
    print(c)
    return max(c.values()) - min(c.values())


if __name__ == '__main__':
    test1 = part1(testInput, 10)
    expected1 = 1588
    print(f"Test part 1 ({expected1}):", test1)
    if test1 == expected1:
        print("Part 1:", part1(myInput, 10))
