#!/usr/bin/python3
'''
Pascal's Triangle
'''


def pascal_triangle(n):
    '''
    Returns an empty list if n <= 0
    You can assume n will be always an integer
    '''
    a = []
    if n <= 0:
        return a
    a = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(a[i - 1]) - 1):
            current = a[i - 1]
            temp.append(a[i - 1][j] + a[i - 1][j + 1])
        temp.append(1)
        a.append(temp)
    return a
