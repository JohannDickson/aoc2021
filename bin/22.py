#! /usr/bin/env python3

import os
import re
from collections import defaultdict


testfile = "../test/22_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.strip() for x in f.readlines()]

inputfile = "../input/22.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.strip() for x in f.readlines()]


def part1(sequence):
    cubes = defaultdict(dict)
    instructions = re.compile(r"(on|off) x=(\-?\d+)\.\.(\-?\d+),y=(\-?\d+)\.\.(\-?\d+),z=(\-?\d+)\.\.(\-?\d+)")
    for step in sequence:
        [ins] = re.findall(instructions, step)
        if ins[0] == "on":
            state = True
        else:
            state = False
        [xmin, xmax, ymin, ymax, zmin, zmax] = [int(x) for x in ins[1:]]

        if not all(
            [abs(xmin) < 50, abs(xmax) < 50, abs(ymin) < 50, abs(ymax) < 50, abs(zmin) < 50, abs(zmax) < 50]
            ):
            continue

        for x in range(xmin, xmax+1):
            if x not in cubes.keys():
                cubes[x] = defaultdict(dict)
            for y in range(ymin, ymax+1):
                if y not in cubes[x].keys():
                    cubes[x][y] = defaultdict(dict)
                for z in range(zmin, zmax+1):
                    cubes[x][y][z] = state

    count=0
    for x in cubes.keys():
        for y in cubes[x].keys():
            for z in cubes[x][y].keys():
                if cubes[x][y][z]:
                    count+=1

    return count


if __name__ == '__main__':
    print("Part 1:", part1(myInput))
