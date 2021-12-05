#! /usr/bin/env python3

import os


testfile = "../test/05_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.strip() for x in f.readlines()]

inputfile = "../input/05.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.strip() for x in f.readlines()]


def findVents(vents, diagonals=False):
    maxX = 0
    maxY = 0
    simpleVents = []
    complexVents = []
    for l in vents:
        start, end = l.split(' -> ')
        startx, starty = [int(z) for z in start.split(',')]
        endx, endy = [int(z) for z in end.split(',')]
        maxX = max([maxX, startx, endx])
        maxY = max([maxY, starty, endy])

        if startx == endx or starty == endy:
            simpleVents.append([startx, starty, endx, endy])
        else:
            complexVents.append([startx, starty, endx, endy])

    ventGrid = []
    for i in range(maxY+1):
        ventGrid.append([])
        for j in range(maxX+1):
            ventGrid[i].append(0)

    for vent in simpleVents:
        for y in range(min(vent[1], vent[3]), max(vent[1], vent[3])+1):
            for x in range(min(vent[0], vent[2]), max(vent[0], vent[2])+1):
                ventGrid[y][x] += 1

    if diagonals:
        for vent in complexVents:
            xdir = 1
            ydir = 1
            if vent[0] > vent[2]:
                xdir = -1
            if vent[1] > vent[3]:
                ydir = -1
            for (y, x) in zip(
                range(vent[1], vent[3]+ydir, ydir),
                range(vent[0], vent[2]+xdir, xdir)
                ):
                    ventGrid[y][x] += 1

    return ventGrid


def part1(vents):
    outvents = findVents(vents)
    score = 0
    for y in outvents:
        score += sum([1 for x in y if x >1])
    return score


def part2(vents):
    outvents = findVents(vents, diagonals=True)
    score = 0
    for y in outvents:
        score += sum([1 for x in y if x >1])
    return score


if __name__ == '__main__':
    print("Part 1:", part1(myInput))
    print("Part 2:", part2(myInput))
