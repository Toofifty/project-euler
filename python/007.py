"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import timer

@timer.many(5)
def main():
    i = 3
    n = 1
    while n < 10001:
        if not any(d for d in range(2, 2 + int(i ** 0.5)) if not i % d):
            n += 1
        i += 2
    return i - 2

main()

# 104743
# 248.4870ms