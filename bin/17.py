#! /usr/bin/env python3

import os
import re


testfile = "../test/17_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = f.read().strip()

inputfile = "../input/17.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = f.read().strip()


def calculatePosition(pos):
    pos['x']+=pos['velocity']['x']
    pos['y']+=pos['velocity']['y']

    pos['maxy'] = max(pos['y'], pos['maxy'])

    if pos['velocity']['x'] > 0:
        pos['velocity']['x']-=1
    elif pos['velocity']['x']<0:
        pos['velocity']['x']+=1

    pos['velocity']['y']-=1

    return pos


def shootHoops(trickshot):
    reg = re.compile(r"target area: x=(\d+)\.\.(\d+), y=(\-\d+)\.\.(\-\d+)")
    [res] = re.findall(reg, trickshot)
    (xmin,xmax,ymin,ymax) = [int(x) for x in res]

    maxIterations = 10

    solutions = []
    for yvel in range(ymin, 100):
        for xvel in range(0, xmax+1):
            pos = {'x': 0, 'y': 0, 'vector':(xvel, yvel), 'velocity':{'x': xvel, 'y':yvel}, 'maxy':0}
            while (pos['x'] < xmax and pos['y'] > ymin):
                pos = calculatePosition(pos)
                if xmin <= pos['x'] <= xmax and ymin <= pos['y'] <= ymax:
                    solutions.append(pos)
                    break

    return max([s['maxy'] for s in solutions]), len(solutions)


def part1(trickshot):
    maxy,_ = shootHoops(trickshot)
    return maxy


def part2(trickshot):
    _,solutions = shootHoops(trickshot)
    return solutions


if __name__ == '__main__':
    print("Part 1:", part1(myInput))
    print("Part 2:", part2(myInput))
