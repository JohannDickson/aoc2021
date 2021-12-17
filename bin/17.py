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


def part1(trickshot):
    print(trickshot)
    reg = re.compile(r"target area: x=(\d+)\.\.(\d+), y=(\-\d+)\.\.(\-\d+)")
    [res] = re.findall(reg, trickshot)
    (xmin,xmax,ymin,ymax) = [int(x) for x in res]

    maxIterations = 100000

    solutions = []
    for yvel in range(0, 100):
        for xvel in range(0, 100):
            pos = {'x': 0, 'y': 0, 'vector':(xvel, yvel), 'velocity':{'x': xvel, 'y':yvel}, 'maxy':0}
            for _ in range(maxIterations):
                pos = calculatePosition(pos)

                if xmin <= pos['x'] <= xmax and ymin <= pos['y'] <= ymax:
                    # print((xmin,xmax,ymin,ymax), pos)
                    solutions.append(pos)
                    break

                if pos['x'] > xmax:
                    break
                if pos['y'] < ymin:
                    break

    from pprint import pprint
    pprint(solutions)

    return max([s['maxy'] for s in solutions])

if __name__ == '__main__':
    test1 = part1(testInput)
    expected1 = 45
    print('test', expected1, test1)
    if test1 == expected1:
        print("Part 1:", part1(myInput))
