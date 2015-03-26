import math
import sys

units = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
}

tens = {
    2 : "twenty",
    3 : "thirty",
    4 : "forty",
    5 : "fifty",
    6 : "sixty",
    7 : "seventy",
    8 : "eighty",
    9 : "ninety",
}

def to_english(n):
    eng_str = ""
    # 256
    hundred = False
    if n > 999:
        return "dunno m8"
    if n > 99:
        digit = math.floor(n / 100) #2
        n -= digit * 100 # 56
        eng_str = eng_str + units[digit] + " hundred "
        hundred = True
    if n > 19:
        digit = math.floor(n / 10) # 5
        n -= digit * 10 # 6
        if hundred: 
            eng_str = eng_str + "and "
            hundred = False
        eng_str = eng_str + tens[int(digit)] + " "
    if n == 0:
        print eng_str,
        return eng_str
    if hundred: eng_str = eng_str + "and "
    eng_str = eng_str + units[int(n)]
    print eng_str,
    return eng_str
    
def count_letters(s):
    c = 0
    for ch in s:
        if ch != " ":
            c += 1
    print c
    return c

sum = 0
for i in range(1, 1000):
    sum += count_letters(to_english(i))
    
sum += count_letters("one thousand")

print sum
        