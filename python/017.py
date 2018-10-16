"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

import math
import timer

units = {
    1: len('one'),
    2: len('two'),
    3: len('three'),
    4: len('four'),
    5: len('five'),
    6: len('six'),
    7: len('seven'),
    8: len('eight'),
    9: len('nine'),
    10: len('ten'),
    11: len('eleven'),
    12: len('twelve'),
    13: len('thirteen'),
    14: len('fourteen'),
    15: len('fifteen'),
    16: len('sixteen'),
    17: len('seventeen'),
    18: len('eighteen'),
    19: len('nineteen'),
}

tens = {
    2: len('twenty'),
    3: len('thirty'),
    4: len('forty'),
    5: len('fifty'),
    6: len('sixty'),
    7: len('seventy'),
    8: len('eighty'),
    9: len('ninety'),
}

hundred = len('hundred')
conj = len('and')

def eng(n):
    digits = 0
    is_hundred = False
    if n > 999:
        return len('onethousand')
    if n > 99:
        digit = n / 100
        n %= 100
        digits += units[digit] + hundred
        is_hundred = True
    if n > 19:
        digit = n / 10
        n %= 10
        if is_hundred:
            digits += conj
            is_hundred = False
        digits += tens[digit]
    if n == 0:
        return digits
    if is_hundred:
        digits += conj
    digits += units[n]
    return digits

@timer.many(100)
def main():
    return sum(eng(i) for i in range(1, 1001))

main()

# 21124
# 0.5479ms