#! /usr/bin/env python3

import os
from math import prod


testfile = "../test/09_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.strip() for x in f.readlines()]

inputfile = "../input/09.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.strip() for x in f.readlines()]


def pad_grid(grid, filler):
    new_grid = [[filler]*(len(grid[0])+2)]
    new_grid += [ [filler]+line+[filler] for line in grid ]
    new_grid += [[filler]*(len(grid[0])+2)]
    return new_grid


def input_to_grid(lines):
    grid = [ [int(x) for x in list(y)] for y in lines]
    grid = pad_grid(grid, 11)
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
                lowpoints.append((y,x))
    return lowpoints


checked_points = set([])
def find_basin_neighbours(grid, point):
    global checked_points

    neighbours = 0
    for pos in [
        (point[0]-1, point[1]),
        (point[0]+1, point[1]),
        (point[0], point[1]-1),
        (point[0], point[1]+1),
        ]:
        if pos not in checked_points and grid[ pos[0] ][ pos[1] ] < 9:
            checked_points.add(pos)
            neighbours += 1
            neighbours += find_basin_neighbours(grid, pos)
    return neighbours


def find_basins(grid, lowpoints):
    basins = []
    for p in lowpoints:
        basin = find_basin_neighbours(grid, p)
        basins.append(basin)
    return basins


def part1(tubes):
    tubes = input_to_grid(tubes)
    lp = find_low_points(tubes)
    lp = [tubes[p[0]][p[1]] for p in lp]
    score = [x+1 for x in lp]
    return sum(score)


def part2(tubes):
    tubes = input_to_grid(tubes)
    lp = find_low_points(tubes)
    basins = find_basins(tubes, lp)
    return prod(sorted(basins)[-3:])


if __name__ == '__main__':
    print("Part 1:", part1(myInput))
    print("Part 2:", part2(myInput))
