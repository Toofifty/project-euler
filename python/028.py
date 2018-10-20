"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

import timer

spiral = 1001

@timer.many(10000)
def main():
    total = 1
    last = 1
    for n in range(2, spiral, 2):
        total += last * 4 + n * 10
        last += n * 4
    return total

main()

# 669171001
# 0.0730ms