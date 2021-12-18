#! /usr/bin/env python3

import os
import json


testfile = "../test/18_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.strip() for x in f.readlines()]

inputfile = "../input/18.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.strip() for x in f.readlines()]


def calculatePosition(pos):
    pos['x']+=pos['velocity']['x']
    pos['y']+=pos['velocity']['y']

    pos['maxy'] = max(pos['y'], pos['maxy'])

    if pos['velocity']['x'] > 0:
        pos['velocity']['x']-=1
    elif pos['velocity']['x']<0:
        pos['velocity']['x']+=1

    pos['velocity']['y']-=1

    return pos


def explode(numbers):
    return None

def reduce(numbers):
    # If any pair is nested inside four pairs, the leftmost such pair explodes.
    # If any regular number is 10 or greater, the leftmost such regular number splits.
    # Once no action in the above list applies, the snailfish number is reduced.


    # To explode a pair, the pair's left value is added to the first regular number to the left of the exploding pair (if any), and the pair's right value is added to the first regular number to the right of the exploding pair (if any). Exploding pairs will always consist of two regular numbers. Then, the entire exploding pair is replaced with the regular number 0.

    # To split a regular number, replace it with a pair; the left element of the pair should be the regular number divided by two and rounded down, while the right element of the pair should be the regular number divided by two and rounded up. For example, 10 becomes [5,5], 11 becomes [5,6], 12 becomes [6,6], and so on.
    return None


def part1(numbers):
    result = 0
    for i in numbers:
        print(json.loads(i))
    return result


if __name__ == '__main__':
    expected1 = None
    test1 = part1(testInput)
    print("Test 1:", expected1, expected1==test1, test1)
    if expected1 == test1:
        print("Part 1:", part1(myInput))
