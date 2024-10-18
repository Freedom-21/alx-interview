#!/usr/bin/python3
"""
This module contains the function
minOperations which calculates the fewest
number of operations needed to reach
exactly n H characters in the file.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations
    to achieve exactly n H characters.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations needed or 0 if not possible.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
