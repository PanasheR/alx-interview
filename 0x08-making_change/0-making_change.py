#!/usr/bin/python3
"""Module determins number of coins for total"""


def makeChange(coins, total):
    """[Given a pile of coins of different values, determine the fewest number
            of coins needed to meet a given amount total]
    Args:
            coins ([list]): [coins is a list of the values of the coins in your
            possession]
            total ([type]): [sum of coins]
    Returns:
            chang [int]: [money left]
    """

    if total <= 0:
        return 0

    # checking the coins out
    if (coins is None or len(coins) == 0):
        return -1

    chang = 0
    m_coin = sorted(coins, reverse=True)
    bd = total

    for coin in m_coin:
        while (bd % coin >= 0 and bd >= coin):
            chang += int(bd / coin)
            bd = bd % coin
    chang = chang if bd == 0 else -1

    return chang
