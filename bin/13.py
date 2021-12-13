#! /usr/bin/env python3

import os
import re


testfile = "../test/13_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = f.read()

inputfile = "../input/13.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = f.read()


def part1(origami):
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
        break

    return len(set(dots))


if __name__ == '__main__':
    print("Part 1:", part1(myInput))
