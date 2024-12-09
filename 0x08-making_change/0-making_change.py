#!/usr/bin/python3
"""
Module for making change
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.

    Args:
        coins (list): List of integers representing coin denominations.
        total (int): The total amount for which change is to be made.

    Returns:
        int: Fewest number of coins needed to meet the total.
             Returns -1 if the total cannot be met by any combination
    """
    if total <= 0:
        return 0

    if not coins:
        return -1

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for coin in coins:
        if coin <= 0:
            continue
        for i in range(coin, total + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1

    return dp[total] if dp[total] <= total else -1
