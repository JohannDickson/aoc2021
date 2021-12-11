#! /usr/bin/env python3

import os


testfile = "../test/11_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.strip() for x in f.readlines()]

inputfile = "../input/11.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.strip() for x in f.readlines()]


has_flashed = set()
def update_energy(grid):
    global has_flashed
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if (y,x) not in has_flashed:
                grid[y][x] += 1
                if grid[y][x] > 9:
                    has_flashed.add((y,x))
                    grid = update_neighbours(grid, (y,x))

    for o in has_flashed:
        (y,x) = o
        grid[y][x] = 0
    has_flashed = set()

    return grid


def update_neighbours(grid, coords):
    global has_flashed
    (y,x) = coords
    neigbhours = [
        (y-1, x-1),
        (y-1, x),
        (y-1, x+1),
        (y, x-1),
        (y, x+1),
        (y+1, x-1),
        (y+1, x),
        (y+1, x+1),
    ]
    for n in neigbhours:
        (ny,nx) = n
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]) and (ny,nx) not in has_flashed:
            grid[ny][nx]+=1
            if grid[ny][nx] >9:
                has_flashed.add((ny,nx))
                grid = update_neighbours(grid, (ny,nx))

    return grid


def print_grid(grid):
    out = ''
    for y in grid:
        out += ''.join([str(x) for x in y])+'\n'
    print(out)


def part1(octopuses, iterations):
    octopuses = [[int(x) for x in list(y)] for y in octopuses]
    flashes = 0
    print_grid(octopuses)
    for i in range(iterations):
        update_energy(octopuses)
        flashes += sum([y.count(0) for y in octopuses])

    return flashes


if __name__ == '__main__':
    print("Part 1:", part1(myInput, 100))

