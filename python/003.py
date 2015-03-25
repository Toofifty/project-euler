"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

num = 600851475143
print max([i for i in range(1, 10000) if num % i == 0])

# 6857