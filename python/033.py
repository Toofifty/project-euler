# -*- coding: utf-8 -*-
"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

https://projecteuler.net/problem=33
"""

import timer

@timer.many(100)
def main():
    num_product = 1
    denom_product = 1
    for i in range(10, 100):
        i1, i2 = [float(n) for n in str(i)]
        if i2 == 0:
            continue
        for j in range(i, 100):
            j1, j2 = [float(n) for n in str(j)]
            fr = float(i) / float(j)
            if i2 == j2 or j2 == 0:
                continue
            if i1 == j1 and i2 / j2 == fr:
                # print 'i1j1', i, j
                num_product *= i
                denom_product *= j
            if i1 == j2 and i2 / j1 == fr:
                # print 'i1j2', i, j
                num_product *= i
                denom_product *= j
            if i2 == j1 and i1 / j2 == fr:
                # print 'i2j1', i, j
                num_product *= i
                denom_product *= j
            if i2 == j2 and i1 / j1 == fr:
                # print 'i2j2', i, j
                num_product *= i
                denom_product *= j
    return denom_product / num_product

main()

# 100
# 2.9969ms