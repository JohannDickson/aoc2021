#! /usr/bin/env python3

import os


testfile = "../test/01_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [int(x) for x in f.readlines()]

inputfile = "../input/01.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [int(x) for x in f.readlines()]


def part1(numbers):
    increased = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i-1]:
            increased +=1
    return increased


def part2(numbers):
    windows = []
    for i in range(0, len(numbers)-2):
        slider = [numbers[i], numbers[i+1], numbers[i+2]]
        windows.append(sum(slider))
    return part1(windows)


if __name__ == '__main__':
    print("Part 1:", part1(myInput))
    print("Part 2:", part2(myInput))
