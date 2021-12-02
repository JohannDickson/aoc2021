#! /usr/bin/env python3

import os


testfile = "../test/02_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.strip() for x in f.readlines()]

inputfile = "../input/02.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.strip() for x in f.readlines()]


def part1(instructions):
    pos = {'x': 0, 'y': 0}
    for i in instructions:
        direction, distance = i.split(' ')
        if direction == "forward":
            pos['x'] += int(distance)
        elif direction == "up":
            pos['y'] -= int(distance)
        elif direction == "down":
            pos['y'] += int(distance)
    return pos['x'] * pos['y']


def part2(instructions):
    pos = {'x': 0, 'y': 0, 'aim': 0}
    for i in instructions:
        direction, distance = i.split(' ')
        if direction == "forward":
            pos['x'] += int(distance)
            pos['y'] += pos['aim']*int(distance)
        elif direction == "up":
            pos['aim'] -= int(distance)
        elif direction == "down":
            pos['aim'] += int(distance)
    return pos['x'] * pos['y']


if __name__ == '__main__':
    print("Part 1:", part1(myInput))
    print("Part 2:", part2(myInput))
