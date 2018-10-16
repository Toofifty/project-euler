"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
from timer import timer_many

@timer_many(1000)
def main():
    return sum([i for i in range(1000) if not i % 3 or not i % 5])

main()

# 233168
# 0.1109ms