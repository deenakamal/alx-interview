#!/usr/bin/python3
""" Prime Game Module """


def isWinner(x, nums):
    """The function returns the name of the player who win """
    maria_wins, ben_wins = 0, 0

    for n in nums:
        primes = prime_sieve(n)
        if not primes:
            ben_wins += 1  # If no primes, Ben wins
            continue

        # Simulate game logic here based on primes
        if len(primes) % 2 == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


def prime_sieve(n):
    """Returns a list of prime numbers up to n."""
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if (is_prime[p] == True):
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    is_prime[0], is_prime[1] = False, False
    primes = [p for p in range(n + 1) if is_prime[p]]
    return primes
