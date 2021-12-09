#! /usr/bin/env python3

import os


testfile = "../test/09_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.strip() for x in f.readlines()]

inputfile = "../input/09.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.strip() for x in f.readlines()]


def input_to_grid(lines):
    grid = [[11]*(len(lines[0])+2)]
    grid += [ [11]+[int(x) for x in list(y)] + [11] for y in lines]
    grid += [[11]*(len(lines[0])+2)]
    return grid


def print_grid(grid):
    out = ''
    for y in grid:
        out += ''.join([str(x) for x in y])+'\n'
    print(out)


def find_low_points(grid):
    lowpoints = []
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] < grid[y-1][x] and grid[y][x] < grid[y+1][x] and grid[y][x] < grid[y][x-1] and grid[y][x] < grid[y][x+1]:
                lowpoints.append({"y": y, "x": x})
    return lowpoints


def part1(tubes):
    tubes = input_to_grid(tubes)
    lp = find_low_points(tubes)
    lp = [tubes[p['y']][p['x']] for p in lp]
    score = [x+1 for x in lp]
    return sum(score)


if __name__ == '__main__':
    print("Part 1:", part1(myInput))
