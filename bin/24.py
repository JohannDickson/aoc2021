#! /usr/bin/env python3

import os
from collections import defaultdict
from math import prod


testfile = "../test/24_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.strip() for x in f.readlines()]

inputfile = "../input/24.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.strip() for x in f.readlines()]


def m_o_n_a_d(instructions, numberInput):
    a = None
    b = None

    inpstr=list(str(numberInput))

    mem = {
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0,
    }

    for ins in instructions:
        action = ins.split(" ", 1)[0]
        ab =  ins.split(" ")[1:]
        # print(action, ab)

        a = int(mem[ab[0]])
        if len(ab) == 2:
            if ab[1] in "qwertyuiopasdfghjklzxcvbnm":
                b = int(mem[ab[1]])
            else:
                b = int(ab[1])

        # print(ins, action, a, b)

        if action == "inp":
            mem[ab[0]] = inpstr.pop(0)
        elif action == "add":
            mem[ab[0]] = sum([a, b])
        elif action == "mul":
            mem[ab[0]] = prod([a, b])
        elif action == "div":
            mem[ab[0]] = a / b
        elif action == "mod":
            mem[ab[0]] = a % b
        elif action == "eql":
            if a == b:
                mem[ab[0]]
            else:
                mem[ab[0]] = 0

    return mem['z']


def part1(instructions, modelno):
    for i in range(99999999999999+1, 10000000000000, -1):
        num = str(i)
        if '0' in num: continue
        res = m_o_n_a_d(instructions, num)
        print(num, res)
        if res == True:
            return i


if __name__ == '__main__':
    print("Part 1:", part1(myInput, 13579246899999))
