#! /usr/bin/env python3

import os


testfile = "../test/03_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.strip() for x in f.readlines()]

inputfile = "../input/03.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.strip() for x in f.readlines()]


def getFreq(chars, tiebreaker=None):
    res = {'0': 0, '1': 0}
    for i in chars:
        res[i] += 1
    if tiebreaker is not None and res['0'] == res['1']:
        return tiebreaker, tiebreaker
    return max(res, key=res.get), min(res, key=res.get)


def rotate(numbers):
    width = len(numbers[0])
    arnold_sideways = [""]*width
    for i in numbers:
        for j in range(0, width):
            arnold_sideways[j] += i[j]
    return arnold_sideways


def part1(numbers):
    width = len(numbers[0])
    sideboard = rotate(numbers)

    gamma = ""
    epsilon = ""
    for i in range(width):
        g, e = getFreq(sideboard[i])
        gamma += g
        epsilon += e

    return int(gamma, 2) * int(epsilon, 2)


def part2(numbers):
    width = len(numbers[0])

    ox = ""
    co2 = ""

    i = 0
    ox_candidates = numbers.copy()
    while len(ox) != width:
        mc, lc = getFreq(rotate(ox_candidates)[i], '1')
        i += 1

        if len(ox) != len(numbers[0]):
            ox += mc
            ox_candidates = [x for x in ox_candidates if x.startswith(ox)]
            if len(ox_candidates) == 1:
                ox = ox_candidates[0]
                break

    i = 0
    co2_candidates = numbers.copy()
    while len(co2) != width:
        mc, lc = getFreq(rotate(co2_candidates)[i], '0')
        i += 1

        if len(co2) != len(numbers[0]):
            co2 += lc
            co2_candidates = [x for x in co2_candidates if x.startswith(co2)]
            if len(co2_candidates) == 1:
                co2 = co2_candidates[0]
                break

    return int(ox, 2) * int(co2, 2)


if __name__ == '__main__':
    print("Part 1:", part1(myInput))
    print("Part 2:", part2(myInput))
