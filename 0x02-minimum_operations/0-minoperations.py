#!/usr/bin/python3


"""
method that calculates the fewest number
of operations needed to result in exactly
n H characters in the file.
"""


def minOperations(n):
    answer = 0
    a = 2
    while n > 1:
        while n % a == 0:
            answer += a
            n /= a
        a += 1
    return answer
