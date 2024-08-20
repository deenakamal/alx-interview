#!/usr/bin/python3
"""
Make change module
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed,
    to meet a given amount total.
    """
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total <= 0:
            break
        count += total // coin
        total %= coin
    return count if total == 0 else -1
