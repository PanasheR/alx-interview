#!/usr/bin/python3
""" You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False """


def canUnlockAll(boxes):
    """ solution for lockbox """
    for box in range(1, len(boxes) - 1):
        read = False
        for index in range(len(boxes)):
            read = (box in boxes[index] and box != index)
            if read:
                break
        if read is False:
            return read
    return True
