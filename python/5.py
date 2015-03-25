"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def c(n):
    return [False for j in range(11, 20) if n % j != 0]
    return True
i = 2520
while c(i): i += 2520
print i

# 232792560