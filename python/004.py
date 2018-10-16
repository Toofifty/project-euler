"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import timer

@timer.many(1000)
def main():
    return max([i * j for i in range(900, 1000) for j in range(900, 1000) if str(i*j) == str(i*j)[::-1]])

main()

# 906609
# 5.6300ms