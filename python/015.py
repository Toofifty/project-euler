"""
Starting in the top left corner of a 2*2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

{img}

How many such routes are there through a 20*20 grid?
"""

import timer
from math import factorial as f

# 1 - 2
# 2 - 6
# 3 - 20
# 4 - 70
# 5 - 252

@timer.many(100000)
def main():
    n = 20
    return f(n * 2) / (f(n) * f(n))

main()

# 137846528820
# 0.0019ms