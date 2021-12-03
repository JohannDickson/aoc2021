#! /usr/bin/env python3

import os


testfile = "../test/03_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.strip() for x in f.readlines()]

inputfile = "../input/03.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.strip() for x in f.readlines()]


def getFreq(chars):
    res = {'0': 0, '1': 0}
    for i in chars:
        res[i] += 1
    return max(res, key=res.get), min(res, key=res.get)


def part1(numbers):
    width = len(numbers[0])
    arnold_sideways = [""]*width

    for i in numbers:
        for j in range(0, width):
            arnold_sideways[j] += i[j]

    gamma = ""
    epsilon = ""
    for i in range(width):
        g, e = getFreq(arnold_sideways[i])
        gamma += g
        epsilon += e

    return int(gamma, 2) * int(epsilon, 2)


if __name__ == '__main__':
    print("Part 1:", part1(myInput))
