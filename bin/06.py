#! /usr/bin/env python3

import os


testfile = "../test/06_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [int(x) for x in f.read().strip().split(',')]

inputfile = "../input/06.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [int(x) for x in f.read().strip().split(',')]


def growfish(school):
    newSchool = school.copy()
    for i in range(len(newSchool)):
        newSchool[i] -=1
        if newSchool[i] < 0:
            newSchool[i] = 6
            newSchool.append(8)
    return newSchool


def part1(lampfish, days):
    for i in range(0, days):
        lampfish = growfish(lampfish)
    return len(lampfish)


if __name__ == '__main__':
    print("Part 1:", part1(myInput, 80))
