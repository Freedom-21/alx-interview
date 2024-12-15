#!/usr/bin/python3
"""The module defines isWinner function."""


def isWinner(x, nums):
    """Determine the winner of the prime game over multiple rounds."""
    if x < 1 or not nums:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums[:x]:
        if n < 2:
            ben_wins += 1
            continue

        prime_count = count_primes_up_to(primes, n)

        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    if ben_wins > maria_wins:
        return "Ben"
    return None


def sieve_of_eratosthenes(limit):
    """Generate a list indicating prime status for numbers up to limit."""
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    for current in range(2, int(limit**0.5) + 1):
        if sieve[current]:
            for multiple in range(current*current, limit + 1, current):
                sieve[multiple] = False
    return sieve


def count_primes_up_to(primes_sieve, n):
    """Count the number of primes up to n using the sieve."""
    return sum(primes_sieve[:n+1])
