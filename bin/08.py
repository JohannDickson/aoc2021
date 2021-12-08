#! /usr/bin/env python3

import os


testfile = "../test/08_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.strip() for x in f.readlines()]

inputfile = "../input/08.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.strip() for x in f.readlines()]


def solveSegments(signals, displays):
    digits = [set(x) for x in displays]
    solved = {}
    seg = {}
    for i in range(len(signals)):
        if len(signals[i]) == 2:
            solved[1] = set(signals[i])
        if len(signals[i]) == 4:
            solved[4] = set(signals[i])
        if len(signals[i]) == 3:
            solved[7] = set(signals[i])
        if len(signals[i]) == 7:
            solved[8] = set(signals[i])


    seg['a'] = solved[7] - solved[1]

    solved[9] = [set(x) for x in signals if len(x)==6 and len(set(x) - (solved[4] | seg['a']))  == 1][0]
    seg['g'] = solved[8] - solved[9]

    seg['e'] = [solved[8] - set(x) for x in signals if len(x)==6 and len(set(x) - (solved[4] | seg['a']))  == 1][0]

    solved[0] = [set(x) for x in signals if len(x)==6 and len(set(x) & (solved[1] | seg['e']))  == 3][0]
    seg['d'] = solved[8] - solved[0]

    seg['b'] = solved[4] - (solved[1] | seg['d'])

    solved[6] = [set(x) for x in signals if len(x)==6 and set(x) not in [solved[0], solved[9]]][0]
    seg['c'] = solved[8] - solved[6]
    seg['f'] = solved[1] - seg['c']

    solved[5] = solved[8] - (seg['c'] | seg['e'])

    solved[2] = solved[8] - (seg['b'] | seg['f'])
    solved[3] = solved[8] - (seg['b'] | seg['e'])

    output = ''
    for d in displays:
        for k,v in solved.items():
            if set(d)==v:
                output+=str(k)
                break

    return int(output)


def part1(segments):
    # digits -> segments:
    # 1 -> 2
    # 4 -> 4
    # 7 -> 3
    # 8 -> 7
    simpleDigits = [2,4,3,7]
    sdc = 0
    for l in segments:
        signals, displays = l.split(' | ')
        signals = signals.split(' ')
        displays = displays.split(' ')
        sdc += sum([1 for x in displays if len(x) in simpleDigits])
    return sdc


def part2(segments):
    sdc = 0
    for l in segments:
        signals, displays = l.split(' | ')
        signals = signals.split(' ')
        displays = displays.split(' ')
        sdc += solveSegments(signals, displays)
    return sdc


if __name__ == '__main__':
    print("Part 1:", part1(myInput))
    print("Part 2:", part2(myInput))
