#! /usr/bin/env python3

import os
from collections import Counter


testfile = "../test/07_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [int(x) for x in f.read().strip().split(',')]

inputfile = "../input/07.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [int(x) for x in f.read().strip().split(',')]


def part1(crabs):
    crabs = Counter(crabs)
    mn = min(crabs)
    mx = max(crabs)
    bestFuel = None
    for i in range(mn, mx+1):
        fuelConsumption = sum([abs(i-p)*c for p,c in crabs.items()])
        if bestFuel == None or fuelConsumption < bestFuel:
            bestFuel = fuelConsumption
    return bestFuel


def part2(crabs):
    crabs = Counter(crabs)
    mn = min(crabs)
    mx = max(crabs)
    bestFuel = None
    for i in range(mn, mx+1):
        fuelConsumption = sum([sum(range(abs(i-p)+1))*c for p,c in crabs.items()])
        if bestFuel == None or fuelConsumption < bestFuel:
            bestFuel = fuelConsumption
    return bestFuel


if __name__ == '__main__':
    print("Part 1:", part1(myInput))
    print("Part 2:", part2(myInput))
