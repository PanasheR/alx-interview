#!/usr/bin/python3
""" Maria and Ben are playing a game """


def isPrime(n):
    """ n: checking prime num"""
    for j in range(2, n):
        if n % j == 0:
            return False
    return True


def remove_numbers(n, nums):
    """ remove numbers """
    for j in range(len(nums)):
        if nums[j] % n == 0:
            nums[j] = 0


def isWinner(x, nums):
    """ where x is number of rounds & nums is n arr
        Return: name of player that won most rounds
        If winner cannot be determined, return None
        You can assume n and x <= 10000
        You cannot import any packages in this task
    """
    nums.sort()
    Ben = 0
    Maria = 0
    for game in range(x):
        nums2 = list(range(1, nums[game] + 1))
        turn = 0
        while True:
            change = False
            for i, n in enumerate(nums2):
                if n > 1 and isPrime(n):
                    remove_numbers(n, nums2)
                    change = True
                    turn += 1
                    break
            if change is False:
                break
        if turn % 2 != 0:
            Maria += 1
        else:
            Ben += 1
    if Maria == Ben:
        return None
    if Maria > Ben:
        return "Maria"
    return "Ben"
