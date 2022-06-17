#!/usr/bin/python3
"""determines if a given data set represents
   a valid UTF-8 encoding
"""


def validUTF8(data):
    """ Each integer represents 1 byte of data """

    sum = 0

    for byte in data:
        binary = bin(byte).replace('0b', '').rjust(8, '0')[-8:]
        if sum == 0:
            if binary.startswith('110'):
                sum = 1
            if binary.startswith('1110'):
                sum = 2
            if binary.startswith('11110'):
                sum = 3
            if binary.startswith('10'):
                return False
        else:
            if not binary.startswith('10'):
                return False
            sum -= 1

    if sum != 0:
        return False

    return True
