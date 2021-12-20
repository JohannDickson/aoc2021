#! /usr/bin/env python3

import os
import json
from copy import deepcopy
from collections import defaultdict

testfile = "../test/20_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = f.read().strip()

inputfile = "../input/20.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = f.read().strip()


def pad_grid(grid, filler):
    new_grid = [[filler]*(len(grid[0])+2)]
    new_grid += [ [filler]+line+[filler] for line in grid ]
    new_grid += [[filler]*(len(grid[0])+2)]
    return new_grid


def print_grid(grid):
    out = ''
    for y in grid:
        for x in y:
            if x =='1':
                out+='#'
            else:
                out+='.'
    print(out)


def updateGrid(grid, algo, filler):
    new_grid = defaultdict(dict, grid)
    oldgrid =deepcopy(grid)
    grid = None
    grid = deepcopy(oldgrid)

    for i in sorted(list(grid.keys())):
        for j in sorted(list(grid[i].keys())):
            substr = ''

            try:
                substr+=grid[i-1][j-1]
            except:
                new_grid[i-1][j-1]=filler
                substr+=filler
            try:
                substr+=grid[i-1][j]
            except:
                new_grid[i-1][j]=filler
                substr+=filler
            try:
                substr+=grid[i-1][j+1]
            except:
                new_grid[i-1][j+1]=filler
                substr+=filler

            try:
                substr+=grid[i][j-1]
            except:
                new_grid[i][j-1]=filler
                substr+=filler
            substr+=grid[i][j]
            try:
                substr+=grid[i][j+1]
            except:
                new_grid[i][j+1]=filler
                substr+=filler

            try:
                substr+=grid[i+1][j-1]
            except:
                new_grid[i+1][j-1]=filler
                substr+=filler
            try:
                substr+=grid[i+1][j]
            except:
                new_grid[i+1][j]=filler
                substr+=filler
            try:
                substr+=grid[i+1][j+1]
            except:
                new_grid[i+1][j+1]=filler
                substr+=filler

            bin_number = int(substr, 2)
            new_number = algo[bin_number]
            new_grid[i][j] = new_number

    return new_grid


def part1(pixels, iterations):
    algo, image = pixels.split('\n\n')
    algo = algo.replace('#', '1').replace('.', '0')

    positions = defaultdict(dict)
    grid = [list(y.strip()) for y in image.strip().split('\n')]
    fill = '0'
    grid = pad_grid(pad_grid(grid, fill),fill)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x]=='#':
                positions[y][x] = '1'
            else:
                positions[y][x] = '0'

    out = ''
    for y in sorted(positions.keys()):
        for x in sorted(positions[y].keys()):
            if positions[y][x] =='1':
                out+='#'
            else:
                out+='.'
        out+='\n'
    print(out)

    # return

    for i in range(iterations):
        print(i, i % 2)
        # positions = deepcopy(updateGrid(deepcopy(positions),algo, str((i) % 2)))
        positions = deepcopy(updateGrid(deepcopy(positions),algo, '0'))
        out = ''
        for y in sorted(positions.keys()):
            for x in sorted(positions[y].keys()):
                if positions[y][x] =='1':
                    out+='#'
                else:
                    out+='.'
            out+='\n'
        print(out)

    result = 0
    for k in positions.keys():
        result+= sum([int(x) for x in positions[k].values()])

    return result


if __name__ == '__main__':
    # expected1 = 35
    # test1 = part1(testInput, 2)
    # print("Test 1:", expected1, expected1==test1, test1)
    # if expected1 == test1:
    print("Part 1:", part1(myInput, 2)) # 5268
