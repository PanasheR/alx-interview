#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.
Write a program that solves the N queens problem.
"""

from sys import argv, exit

global N

if len(argv) > 2 or len(argv) == 1:
    print("Usage: nqueens N")
    exit(1)

N = int(argv[1])

if not isinstance(N, int):
    print("N must be a number")
    exit(1)

if N < 4:
    print("N must be at least 4")
    exit(1)


def queens(n, i, a, b, c):
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


for solution in queens(N, 0, [], [], []):
    result = []
    for i in range(len(solution)):
        result.append([i, solution[i]])
    print(result)
