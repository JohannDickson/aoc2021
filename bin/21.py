#! /usr/bin/env python3

import os
from collections import deque


testfile = "../test/21_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = f.read().strip()

inputfile = "../input/21.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = f.read().strip()



def part1(positions, gameboard, dice):
    players = [int(p[-1]) for p in positions.split('\n')]
    pawns = [
        deque(range(1, gameboard+1)),
        deque(range(1, gameboard+1)),
    ]

    for i in range(len(players)):
        pawns[i].rotate(- pawns[i].index(players[i]))

    turns = 3
    scores = [0,0]
    dice = deque(range(1, 101))
    whoseturn = deque([0,1])
    turnsplayed = 0
    while not any(x >= 1000 for x in scores):
        turnsplayed+=turns
        whosturnisit = whoseturn[0]
        whoseturn.rotate(1)

        rolls = [dice[0], dice[1], dice[2]]
        dice.rotate(-3)
        moves = sum(rolls)
        pawns[whosturnisit].rotate(- moves)
        box = pawns[whosturnisit][0]
        scores[whosturnisit] += box
        # print("turn", i, "player", whosturnisit, rolls, box, scores[whosturnisit])
        # print(scores[whosturnisit])

        if scores[whosturnisit] >= 1000:
            break

    print(scores, turnsplayed)

    return min(scores)*turnsplayed


if __name__ == '__main__':
    test1 = part1(testInput, 10, 100)
    expected1 = 739785
    print(f"Test part 1 ({expected1}):", test1)
    if test1 == expected1:
        print("Part 1:", part1(myInput, 10, 100))
