# -*- coding: utf-8 -*-
"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

https://projecteuler.net/problem=32
"""

import timer

pandigital = [str(n) for n in range(1, 10)]

def is_pandigital(*args):
    return sorted(''.join(str(n) for n in args)) == pandigital


@timer.many(1)
def main():
    products = []
    for i in range(50):
        for j in range(2000):
            if i * j > 9999 or i * j < 1000:
                continue
            if is_pandigital(i, j, i * j):
                products.append(i * j)
    return sum(set(products))

main()

# 45228
# 57.1949ms