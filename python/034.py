# -*- coding: utf-8 -*-
"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

https://projecteuler.net/problem=34
"""

import timer

def fac(n):
    if n <= 1:
        return 1
    return n * fac(n - 1)

def is_curious(num):
    return sum(fac(int(n)) for n in str(num)) == num

@timer.many(1)
def main():
    return sum(n for n in range(3, 100000) if is_curious(n))

main()

# 40730
# 401.6590ms