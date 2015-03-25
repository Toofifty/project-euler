"""
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

# next collatz
def co(n):
    if n % 2: # odd
        return 3 * n + 1
    return n / 2

# chain length
def cl(n):
    #print n
    i = 1
    while n > 1:
        i += 1
        n = co(n)
    return i

l = 0
s = 0
for n in range(500001, 1000000, 2):
    c = cl(n)
    if c > l:
        l = c
        s = n
print s, l