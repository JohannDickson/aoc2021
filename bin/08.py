#! /usr/bin/env python3

import os


testfile = "../test/08_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.strip() for x in f.readlines()]

inputfile = "../input/08.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.strip() for x in f.readlines()]


def part1(segments):
    # digits -> segments:
    # 1 -> 2
    # 4 -> 4
    # 7 -> 3
    # 8 -> 7
    simpleDigits = [2,4,3,7]
    sdc = 0
    for l in segments:
        signals, displays = l.split(' | ')
        signals = signals.split(' ')
        displays = displays.split(' ')
        sdc += sum([1 for x in displays if len(x) in simpleDigits])
    return sdc


if __name__ == '__main__':
    print("Part 1:", part1(myInput))
