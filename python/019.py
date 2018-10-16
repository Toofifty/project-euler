"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

import timer

months = [
    31, # jan
    28, # feb
    31, # mar
    30, # apr
    31, # may
    30, # jun
    31, # jul
    31, # aug
    30, # sep
    31, # oct
    30, # nov
    31, # dec
]

MONDAY = 0
SUNDAY = 6

def sundays(year, day):
    sundays = 0
    months[1] = 29 if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) else 28
    for month in months:
        if day % 7 == SUNDAY:
            sundays += 1
        day += month
    return sundays, day

@timer.many(1000)
def main():
    total = 0
    _, day = sundays(1900, MONDAY)
    for year in range(1901, 2001):
        count, day = sundays(year, day)
        total += count
    return total

main()

# 171
# 0.1450ms