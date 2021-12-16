#! /usr/bin/env python3

import os
from math import prod


testfile = "../test/16_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.strip() for x in f.readlines()]

inputfile = "../input/16.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = f.read().strip()


hexmap = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def readPacket(packet):
    version = int(packet[:3], 2)
    type_id = int(packet[3:6], 2)

    if type_id == 4: # value
        number_chunk = list(packet[6:])

        the_number = ''
        is_last = None

        while is_last != '0':
            is_last = number_chunk.pop(0)
            if is_last == '1':
                the_number += ''.join([number_chunk.pop(0) for x in range(4)])
            elif is_last == '0':
                the_number += ''.join([number_chunk.pop(0) for x in range(4)])

        return ((version, type_id, int(the_number, 2)), ''.join(number_chunk))

    else:
        length_type_id = int(packet[6:7], 2)
        contents = packet[7:]
        subs = []

        if length_type_id == 0:
            total_length_in_bits = int(contents[:15], 2)
            nextpacket = contents[15:15+total_length_in_bits]
            while nextpacket != '':
                (res, nextpacket) = readPacket(nextpacket)
                subs.append(res)
            next_step = contents[15+total_length_in_bits:]

        elif length_type_id == 1:
            number_of_sub_packets = int(contents[:11], 2)
            nextpacket=contents[11:]
            for i in range(number_of_sub_packets):
                (res, nextpacket) = readPacket(nextpacket)
                subs.append(res)
            next_step = nextpacket

        version += sum([p[0] for p in subs])

        values = [x[2] for x in subs]
        if type_id == 0: # sum
            result = sum(values)

        if type_id == 1: # product
            result = prod(values)

        if type_id == 2: # minimum
            result = min(values)

        if type_id == 3: # maximum
            result = max(values)

        if type_id == 5: # >
            result = 1 if (values[0] > values[1]) else 0

        if type_id == 6: # <
            result = 1 if (values[0] < values[1]) else 0

        if type_id == 7: # ==
            result = 1 if (values[0] == values[1]) else 0

        return ((version, type_id, result), next_step)


def part1(hexinput):
    binstring = ''.join([hexmap[c] for c in hexinput])
    result, _ = readPacket(binstring)
    return(result[0])


def part2(hexinput):
    binstring = ''.join([hexmap[c] for c in hexinput])
    result, _ = readPacket(binstring)
    return(result[2])


if __name__ == '__main__':
    print("Part 1:", part1(myInput))
    print("Part 2:", part2(myInput))
