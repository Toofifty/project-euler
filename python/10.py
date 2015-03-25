"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

i = 3
t = 2
while i < 2000000:
    if not any(d for d in range(2, 2+int(i**0.5)) if not i % d): t+=i
    i+=1
print t

# 142913828922