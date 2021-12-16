#! /usr/bin/env python3

import os


testfile = "../test/16_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.strip() for x in f.readlines()]

inputfile = "../input/16.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.strip() for x in f.readlines()]

subPacket = None
versionSum = 0
def readPacket(packet):
    global versionSum, subPacket

    version = int(packet[:3], 2)
    versionSum+=version
    type_id = int(packet[3:6], 2)
    print("Version", version, type_id)

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

        if subPacket is not None:
            subPacket = ''.join(number_chunk)
            print("REMAINDER", subPacket)

        value = int(the_number, 2)

    else:
        length_type_id = int(packet[6:7], 2)
        contents = packet[7:]
        print("Operator", length_type_id)
        if  length_type_id == 0:
            total_length_in_bits = int(contents[:15], 2)
            sub_packet = contents[15:15+total_length_in_bits]
            # Identify multiple sub packets
            subPacket = sub_packet
            while subPacket is not None:
                print("Sub", total_length_in_bits, sub_packet)
                print(readPacket(sub_packet))

        elif length_type_id == 1:
            number_of_sub_packets = int(contents[:11], 2)
            sub_packet=contents[11:]
            print("Sub", number_of_sub_packets, sub_packet)
            for i in range(number_of_sub_packets):
                print(readPacket(sub_packet))
                sub_packet = subPacket

        value = 0

    return value


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

def part1(hexinput):
    print(hexinput)
    binstring = ''.join([hexmap[c] for c in hexinput])
    val = readPacket(binstring)

    return val


if __name__ == '__main__':
    for t in testInput:
        print(part1(t))
        versionSum = 0
        # break
    expected1 = part1(t[-1])
    print(f"Test part 1 ({expected1}):", test1)
    if test1 == expected1:
        print("Part 1:", part1(myInput))
