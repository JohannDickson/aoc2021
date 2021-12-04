#! /usr/bin/env python3

import os


def parseInput(input):
    sections = input.rstrip().split("\n\n")
    numbers = sections[0].split(',')
    boards = [b.split('\n') for b in sections[1:]]
    for b in boards:
        for l in range(len(b)):
            b[l] = b[l].split()
    return [numbers, boards]

testfile = "../test/04_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = f.read()

inputfile = "../input/04.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = f.read()


def playBingo(bingo):
    numbers = bingo[0]
    boards = bingo[1]
    winner = None

    while len(numbers) > 0 and winner is None:
        called = numbers.pop(0)
        for i in range(len(boards)):
            for y in range(len(boards[i])):
                for x in range(len(boards[i][y])):
                    if boards[i][y][x] == called:
                        boards[i][y][x] = ''

                    if all([z[x] == '' for z in boards[i]]):
                        winner = i
                        break

                if all([z == '' for z in boards[i][y]]):
                    winner = i
                    break

    winningSum = 0
    for i in boards[winner]:
        winningSum += sum([int(x) for x in i if x!=''])

    return winningSum * int(called)


def part1(input):
    bingo = parseInput(input)
    return playBingo(bingo)


if __name__ == '__main__':
    print("Part 1:", part1(myInput))
