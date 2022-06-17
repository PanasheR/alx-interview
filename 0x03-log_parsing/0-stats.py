#!/usr/bin/python3
"""Write a script that reads stdin line by line
   and computes metrics
"""
from sys import stdin


def display_msg(codes, file_size):
    print("File size: {}".format(file_size))
    for key, val in sorted(codes.items()):
        if val != 0:
            print("{}: {}".format(key, val))


f_size = 0
cod = 0
lines = 0
codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            lines += 1

            if lines <= 10:
                f_size += int(parsed_line[0])
                cod = parsed_line[1]

                if (cod in codes.keys()):
                    codes[cod] += 1

            if (lines == 10):
                display_msg(codes, f_size)
                lines = 0

finally:
    display_msg(codes, f_size)
