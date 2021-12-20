#! /usr/bin/env python3

import os
import json
from collections import defaultdict

testfile = "../test/20_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = f.read().strip()

inputfile = "../input/20.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = f.read().strip()


def print_grid(grid):
    out = ''
    for y in grid:
        out += ''.join([str(x) for x in y])+'\n'
    print(out)


def updateGrid(grid, algo):
    new_grid = grid

    # from pprint import pprint
    # pprint(grid)
    for i in list(grid.keys()):
        for j in list(grid[i].keys()):
            substr = ''

            try:
                substr+=grid[i-1][j-1]
            except:
                grid[i-1][j-1]='0'
                substr+='0'
            try:
                substr+=grid[i-1][j]
            except:
                grid[i-1][j]='0'
                substr+='0'
            try:
                substr+=grid[i-1][j+1]
            except:
                grid[i-1][j+1]='0'
                substr+='0'

            try:
                substr+=grid[i][j-1]
            except:
                grid[i][j-1]='0'
                substr+='0'
            substr+=grid[i][j]
            try:
                substr+=grid[i][j+1]
            except:
                grid[i][j+1]='0'
                substr+='0'

            try:
                substr+=grid[i+1][j-1]
            except:
                grid[i+1][j-1]='0'
                substr+='0'
            try:
                substr+=grid[i+1][j]
            except:
                grid[i+1][j]='0'
                substr+='0'
            try:
                substr+=grid[i+1][j+1]
            except:
                grid[i+1][j+1]='0'
                substr+='0'

            bin_number = int(substr, 2)
            new_number = algo[bin_number]
            new_grid[i][j] = new_number

    return new_grid


def part1(pixels):
    algo, image = pixels.split('\n\n')
    algo = algo.replace('#', '1').replace('.', '0')

    positions = defaultdict(dict)
    grid = [y.strip() for y in image.strip().split('\n')]
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x]=='#':
                positions[y][x] = '1'
            else:
                positions[y][x] = '0'


    result = 0
    for k in positions.keys():
        result+= sum([int(x) for x in positions[k].values()])
    print(result)
    positions = updateGrid(positions,algo)
    result = 0
    for k in positions.keys():
        result+= sum([int(x) for x in positions[k].values()])
    print(result, 23)

    positions = updateGrid(positions,algo)

    result = 0
    for k in positions.keys():
        result+= sum([int(x) for x in positions[k].values()])
    print(result, 35)

    return result


if __name__ == '__main__':
    expected1 = 35
    test1 = part1(testInput)
    print("Test 1:", expected1, expected1==test1, test1)
    if expected1 == test1:
        print("Part 1:", part1(myInput))
