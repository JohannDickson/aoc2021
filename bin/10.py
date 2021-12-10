#! /usr/bin/env python3

import os


testfile = "../test/10_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.strip() for x in f.readlines()]

inputfile = "../input/10.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.strip() for x in f.readlines()]


pairs = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>',
}


def part1(chunks):
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    score = 0
    for l in chunks:
        expected = []
        for c in list(l):
            if c in pairs.keys():
                expected.append(pairs[c])
            elif c == expected[-1]:
                del expected[-1]
            else:
                score += points[c]
                break
    return score


if __name__ == '__main__':
    print("Part 1:", part1(myInput))
