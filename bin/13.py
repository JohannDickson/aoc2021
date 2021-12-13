#! /usr/bin/env python3

import os
import re


testfile = "../test/13_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = f.read()

inputfile = "../input/13.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = f.read()


def fold_paper(origami, onefold=False):
    [dotsCoords, instructions] = origami.strip().split('\n\n')
    dots = []
    for dot in dotsCoords.split('\n'):
        x,y = dot.split(',')
        dots.append( (int(y), int(x)) )

    for instruction in instructions.split('\n'):
        finder = re.compile("fold along ([xy])=([0-9]+)")
        [(axis,coord)] = re.findall(finder, instruction)
        coord = int(coord)

        for i in range(len(dots)):
            (y,x) = dots[i]
            if axis == 'y' and y > coord:
                dots[i] = (coord-abs(coord-y), x)
            if axis == 'x' and x > coord:
                dots[i] = (y, coord-abs(coord-x))

        if onefold:
            return len(set(dots))

    maxX = max([x for (y,x) in dots]) +1
    maxY = max([y for (y,x) in dots]) +1
    grid = [[' ' for x in range(maxX)] for y in range(maxY)]

    for (y,x) in dots:
        grid[y][x] = '#'

    out = '\n'
    for y in grid:
        out += ''.join([str(x) for x in y])+'\n'

    return out


def part1(origami):
    return fold_paper(origami, True)


def part2(origami):
    return fold_paper(origami, False)


if __name__ == '__main__':
    print("Part 1:", part1(myInput))
    print("Part 2:", part2(myInput))
