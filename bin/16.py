#! /usr/bin/env python3

import os


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


versionSum = 0
def readPacket(packet):
    global versionSum

    version = int(packet[:3], 2)
    type_id = int(packet[3:6], 2)

    versionSum+=version

    if type_id == 4:
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
            return ((version, type_id, subs), contents[15+total_length_in_bits:])

        elif length_type_id == 1:
            number_of_sub_packets = int(contents[:11], 2)
            nextpacket=contents[11:]
            for i in range(number_of_sub_packets):
                (res, nextpacket) = readPacket(nextpacket)
                subs.append(res)
            return ((version, type_id, subs), nextpacket)


def part1(hexinput):
    global versionSum
    versionSum = 0
    binstring = ''.join([hexmap[c] for c in hexinput])
    readPacket(binstring)
    return versionSum


if __name__ == '__main__':
    print("Part 1:", part1(myInput))
