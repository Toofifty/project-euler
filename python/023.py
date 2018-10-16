"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

import timer
import math

cache = {}

def is_abundant(n):
    if n in cache:
        return cache[n]
    cache[n] = sum(f for f in range(1, n) if n % f == 0) > n
    return cache[n]

def abundant_sum(num):
    # brute force
    for c in range(12, num / 2):
        if is_abundant(c) and is_abundant(num - c):
            return True
    # print num
    return False

# total = sum(i for i in range(24, 21000) if not abundant_sum(i))

# warm cache >:)
for i in range(20000): is_abundant(i)

@timer.many(1)
def main():
    return sum(i for i in range(24, 21284) if not abundant_sum(i))

main()

# 4179871
# 18882.25ms