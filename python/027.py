"""
Euler discovered the remarkable quadratic formula:

n2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0<=n<=39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2-79n+1601 was discovered, which produces 80 primes for the consecutive values 0<=n<=79. The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|<=1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |-4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
"""

import timer

def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            return False
    return True

def prime_range(a, b):
    n = 0
    while True:
        if not is_prime(n ** 2 + a * n + b):
            return n
        n += 1

@timer.many(1)
def main():
    # brute force
    best = 0
    coeff = (0, 0)
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            if b - a < 0:
                continue
            pr = prime_range(a, b)
            if pr > best:
                best = pr
                coeff = (a, b)
    return coeff[0] * coeff[1]

main()

# -59231
# 2543.8900ms