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
    decreased = 0
    prev = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > prev:
            increased +=1
        elif numbers[i] < prev:
            decreased +=1
        else:
            print("huh?")
        prev = numbers[i]
    print(increased)
    print(decreased)

part1(myInput)
