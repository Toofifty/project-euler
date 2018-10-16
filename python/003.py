"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from timer import timer_many

@timer_many(1000)
def main():
    num = 600851475143
    return max([i for i in range(1, 10000) if num % i == 0])

main()

# 6857
# 0.5929ms