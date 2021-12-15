#! /usr/bin/env python3

import os
from collections import Counter


testfile = "../test/14_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = f.read()

inputfile = "../input/14.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = f.read()


def part1(polymers, iterations):
    [poly, rules] = polymers.strip().split('\n\n')
    changes = []

    for r in rules.split('\n'):
        pair, new = r.split(' -> ')
        changes.append((pair, new))

    pair_counter = Counter()
    c = Counter(poly)
    for i in range(len(poly)-1):
        if poly[i:i+2] not in pair_counter:
            pair_counter[ poly[i:i+2] ] = 1
        else:
            pair_counter[ poly[i:i+2] ] += 1

    for _ in range(iterations):
        before_split = pair_counter.copy()
        for (pair, new) in changes:
            if pair in pair_counter:
                pair_counter[pair] -= before_split[pair]
                pair_counter[pair[0]+new] += before_split[pair]
                pair_counter[new+pair[1]] += before_split[pair]
                c[new] += before_split[pair]

    return max(c.values()) - min(c.values())


if __name__ == '__main__':
    print("Part 1:", part1(myInput, 10))
    print("Part 2:", part1(myInput, 40))
