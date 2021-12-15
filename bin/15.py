#! /usr/bin/env python3

import os


testfile = "../test/15_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [[int(x) for x in y.strip()] for y in f.readlines()]

inputfile = "../input/15.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [[int(x) for x in y.strip()] for y in f.readlines()]


def part1(grid):
    # Call a friend: Dijkstra
    return None


if __name__ == '__main__':
    test1 = part1(testInput)
    expected1 = 40
    print(f"Test part 1 ({expected1}):", test1)
    if test1 == expected1:
        print("Part 1:", part1(myInput))
