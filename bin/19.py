#! /usr/bin/env python3

import os
import json
from math import ceil, floor


testfile = "../test/18_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.strip() for x in f.readlines()]

inputfile = "../input/18.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.strip() for x in f.readlines()]


def find_deepest(numbers):
    for i in range(len(numbers)):
        if type(numbers[i]) == list:
            for j in range(len(numbers[i])):
                # print(j, numbers[i][j])
                if type(numbers[i][j]) == list:
                    for k in range(len(numbers[i][j])):
                        # print(k, numbers[i][j][k])
                        if type(numbers[i][j][k]) == list:
                            for l in range(len(numbers[i][j][k])):
                                # print(l, numbers[i][j][k][l])
                                if type(numbers[i][j][k][l]) == list:
                                    return [i,j,k,l]
    return False


def find_lengths(numbers, deep):
    [i,j,k,l] = deep
    lengths = []
    lengths.append(len(numbers[i]))
    lengths.append(len(numbers[i][j]))
    lengths.append(len(numbers[i][j][k]))
    lengths.append(len(numbers[i][j][k][l]))
    return lengths


def explode(numbers, deep, lengths):
    [i,j,k,l] = deep
    [a, b] = numbers[i][j][k][l]
    prev=lengths[4]
    for i in range(len(lengths)-1, -1, -1):

        print(lengths, i-1)



    return numbers


def find_10(numbers):
    for i in range(len(numbers)):
        if type(numbers[i])==int and numbers[i] >= 10:
            return [i]
            for j in range(len(numbers[i])):
                if type(numbers[i][j])==int and numbers[i][j] >= 10:
                    return [i,j]
                    for k in range(len(numbers[i][j])):
                        if type(numbers[i][j][k])==int and numbers[i][j][k] >= 10:
                            return [i,j,k]
                            for l in range(len(numbers[i][j][k])):
                                if type(numbers[i][j][k][l])==int and numbers[i][j][k][l] >= 10:
                                    return [i,j,k,l]
    return False


def split(n):
    a = floor(n/2)
    b = ceil(n/2)
    return [a, b]


def reduce(numbers):
    # If any pair is nested inside four pairs, the leftmost such pair explodes.
    # If any regular number is 10 or greater, the leftmost such regular number splits.
    # Once no action in the above list applies, the snailfish number is reduced.

    deep = find_deepest(numbers)
    ten = find_10(numbers)
    while deep or ten:
        # To explode a pair, the pair's left value is added to the first regular number to the left of the exploding pair (if any), and the pair's right value is added to the first regular number to the right of the exploding pair (if any). Exploding pairs will always consist of two regular numbers. Then, the entire exploding pair is replaced with the regular number 0.
        if deep:
            print(deep)
            lengths = find_lengths(numbers, deep)
            print('deep', deep)
            print('leng', lengths)

            numbers = explode(numbers, deep, lengths)

        # To split a regular number, replace it with a pair; the left element of the pair should be the regular number divided by two and rounded down, while the right element of the pair should be the regular number divided by two and rounded up. For example, 10 becomes [5,5], 11 becomes [5,6], 12 becomes [6,6], and so on.
        if ten:
            print('TEN', ten)
            if len(ten) > 1:
                if len(ten) > 2:
                    if len(ten) > 3:
                        numbers[ten[0]][ten[1]][ten[2]][ten[3]] = split(numbers[ten[0]][ten[1]][ten[2]][ten[3]])
                    else:
                        numbers[ten[0]][ten[1]][ten[2]] = split(numbers[ten[0]][ten[1]][ten[2]])
                else:
                    numbers[ten[0]][ten[1]] = split(numbers[ten[0]][ten[1]])
            else:
                numbers[ten[0]] = split(numbers[ten[0]])

        deep = find_deepest(numbers)
        ten = find_10(numbers)

    return numbers


def part1(numbers):
    result = 0
    for i in numbers:
        print(json.loads(i))
        reduce(json.loads(i))
    return result


if __name__ == '__main__':
    expected1 = None
    test1 = part1(testInput)
    print("Test 1:", expected1, expected1==test1, test1)
    if expected1 == test1:
        print("Part 1:", part1(myInput))
