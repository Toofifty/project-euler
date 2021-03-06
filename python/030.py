# -*- coding: utf-8 -*-
"""

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

https://projecteuler.net/problem=30
"""

import timer

def sum_of_powers(n):
    return n == sum(int(d) ** 5 for d in str(n))

@timer.many(10)
def main():
    return sum(n for n in range(2, 200000) if sum_of_powers(n))

main()

# 443839
# 799.1529ms