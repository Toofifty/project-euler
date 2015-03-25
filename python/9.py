"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

# Rearrange!
# [1] a^2 + b^2 - c^2 = 0
# [1] c^2 = a^2 + b^2
# [2] c^2 = (1000 - a - b)^2
# [1+2] (1000 - a - b)^2 = a^2 + b^2
# [1+2] 1,000,000 - 1000a - 1000b - 1000a + a^2 + ab - 1000b + ab + b^2 = a^2 + b^2
# [1+2] 1,000,000 - 2000a - 2000b + 2ab = 0
# [1+2] ab = -500,000 + 1000a + 1000b
# [1+2] ab - 1000a = 1000b - 500,000
# [1+2] a(b - 1000) = 1000b - 500,000
# [1+2] a = 1000(b - 500)/(b - 1000)

# [>n] a = n(b - 500)/(b - 1000)

# Now: use b to find a
# Then: c = 1000 - a - b

for b in range(500):
    a=1000*(b-500)/(b-1000)
    c=1000-a-b
    if a<b and b<c and a*a+b*b==c*c: 
        print a,b,c,a*b*c
        break

# 31875000