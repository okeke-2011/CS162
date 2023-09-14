import math
import random
import numpy as np

# BIGFACTOR represents the product of all prime factors under 100.  This allows
# us to do a fast pre-check and immediately eliminate any numbers which are
# divisible by a small number

SMALLPRIMES = []
BIGFACTOR = 1
for num in range(1, 100):
    if math.gcd(BIGFACTOR, num) == 1:
        BIGFACTOR = BIGFACTOR * num
        SMALLPRIMES.append(num)
SMALLPRIMES = set(SMALLPRIMES)


def is_prime(x):
    """ Test whether x is a prime number."""
    # Check for all possible prime factors under 100:
    if x in SMALLPRIMES:
        return True

    if math.gcd(x, BIGFACTOR) != 1:
        return False
    # The fast check failed, now perform exhaustive check.
    max_factor = int(math.sqrt(x))
    for a in range(101, max_factor, 100):
        if x % a == 0:
            return False
    return True


def get_next_prime(x):
    """ Find the smallest prime number which is greater than or equal to x."""
    x = int(x)
    if x % 2 == 0:
        x = x + 1

    while not is_prime(x):
        x = x + 2

    return x


def miller_rabin(n, k):
    "Probabilistic prime testing."
    # Implementation uses the Miller-Rabin Primality Test
    # The optimal number of rounds (k) for this test is 40
    # See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    # for justification

    # If number is even, it's a composite number

    if n == 2 or n == 3:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1

        # integer division
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)

        # (a^s)%n
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

