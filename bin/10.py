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


def part2(chunks):
    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    scores = []
    for l in chunks:
        expected = []
        corrupt = False
        for c in list(l):
            if c in pairs.keys():
                expected.append(pairs[c])
            elif c == expected[-1]:
                del expected[-1]
            else:
                corrupt = True
                break

        if not corrupt:
            score = 0
            for c in expected[::-1]:
                score *= 5
                score += points[c]
            scores.append(score)

    return sorted(scores)[(len(scores)-1)//2]


if __name__ == '__main__':
    print("Part 1:", part1(myInput))
    print("Part 2:", part2(myInput))
