#! /usr/bin/env python3

import os


testfile = "../test/05_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.strip() for x in f.readlines()]

inputfile = "../input/05.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.strip() for x in f.readlines()]


def findVents(vents):
    maxX = 0
    maxY = 0
    simpleVents = []
    for l in vents:
        start, end = l.split(' -> ')
        startx,starty = start.split(',')
        endx,endy = end.split(',')

        if startx == endx or starty == endy:
            startx = int(startx)
            endx = int(endx)
            starty = int(starty)
            endy = int(endy)

            simpleVents.append([startx, starty, endx, endy])

            maxX = max([maxX, startx, endx])
            maxY = max([maxY, starty, endy])

    ventGrid = []
    for i in range(maxY+1):
        ventGrid.append([])
        for j in range(maxX+1):
            ventGrid[i].append(0)

    for vent in simpleVents:
        for y in range(min(vent[1], vent[3]), max(vent[1], vent[3])+1):
            for x in range(min(vent[0], vent[2]), max(vent[0], vent[2])+1):
                ventGrid[y][x] += 1

    return ventGrid


def part1(vents):
    outvents = findVents(vents)
    score = 0
    for y in outvents:
        score += sum([1 for x in y if x >1])
    return score


if __name__ == '__main__':
    print("Part 1:", part1(myInput))
