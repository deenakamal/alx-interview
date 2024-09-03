#!/usr/bin/python3
"""Prime Game Module"""


def isWinner(x, nums):
    """Determine the winner of the prime game."""
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    primes = prime_sieve(max_n)
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if sum(primes[0:n+1]) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


def prime_sieve(n):
    """Returns a list where index i is True if i is a prime number."""
    sieve = [True] * (n + 1)
    sieve[0], sieve[1] = False, False
    p = 2
    while (p * p <= n):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
        p += 1
    return sieve
