#!/usr/bin/python

#
# Convert a date in the Amazigh Calendar to a Julian Day
#

import months

def convert(day, month, year):

    day = int(day)
    month = month
    year = int(year)
    alpha = 0
    days = 0

    if year > 0:
        # positive years.
        alpha = 1374434
        for y in range(1,year):
            if (y + 2) % 4 == 0:
                days += 366
            else:
                days += 365

        if (year + 2) % 4 == 0:
            # leap year
            m = months.AMAZIGH_MONTHS_LEAP
        else:
            # not a leap year
            m = months.AMAZIGH_MONTHS_NORMAL

        for i in m.keys():
            if i == month:
                days += day
                break
            else:
                days += m[i]

    else:
        # negative years.
        alpha = 1374435
        year = 0 - year

        if (year + 2) % 4 == 0:
            # leap yar
            m = months.AMAZIGH_MONTHS_LEAP
        else:
            # not a leap year
            m = months.AMAZIGH_MONTHS_NORMAL

        for i in m.keys():
            if i == month:
                days += day - 1
                break
            else:
                days += m[i]

        for y in range(0, year):
            if (y + 2) % 4 == 0:
                days -= 366
            else:
                days -= 365

    jday = alpha + days
    return jday
