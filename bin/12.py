#! /usr/bin/env python3

import os


testfile = "../test/12_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.strip() for x in f.readlines()]

inputfile = "../input/12.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.strip() for x in f.readlines()]


def visit_caves(cave_map, from_point, caves_visited):
    paths = []

    visited = caves_visited.copy()
    if from_point == from_point.lower():
        visited.add(from_point)

    current_path = [from_point]

    pre_con = visited.copy()
    for connector in sorted(cave_map[from_point] - pre_con):
        visited = pre_con.copy()

        if connector == 'end':
            current_path.append(connector)
            paths.append(current_path)

        elif connector not in visited:
            if connector == connector.lower():
                visited.add(connector)

            next_steps = visit_caves(cave_map, connector, visited)
            for nxt in next_steps:
                branch = current_path + [nxt]
                paths.append(branch)

    return paths


def part1(caves):
    cave_map = {}
    for c in caves:
        a,b = c.split('-')
        if a in cave_map:
            cave_map[a].add(b)
        else:
            cave_map[a] = set([b])
        if b in cave_map:
            cave_map[b].add(a)
        else:
            cave_map[b] = set([a])

    from pprint import pprint
    pprint(cave_map)
    routes = visit_caves(cave_map, 'start', set())
    print()
    pprint(routes)
    return len(routes)


if __name__ == '__main__':
    test1 = part1(testInput)
    expected1 = 10
    print(f"Test part 1 ({expected1}):", test1)
    if test1 == expected1:
        print("Part 1:", part1(myInput))
