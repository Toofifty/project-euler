"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import timer

@timer.many(1)
def main():
    i = 3
    t = 2
    while i < 2000000:
        if not any(d for d in range(2, 2 + int(i ** 0.5)) if not i % d):
            t += i
        i += 1
    return t

main()

# 142913828922
# 23883.4720ms