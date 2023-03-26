#!/usr/bin/python

# Convert between the True Hindu solar calendar and Julian Day

from math import floor, ceil
from fractions import Fraction
from months import NUM_HINDU as NUMON
from months import HINDU_NUM as MONTHNO
from hindu_functions import uj_lon as lon
from hindu_functions import uj_lat as lat
from hindu_functions import sunrise, creation, sid_year, ntime, rasi
from hindu_functions import ky as epoch

def suncheck(jday):
    '''Check if a given instant is before or after sunrise'''
    jday = Fraction(jday)
    dawn = sunrise(jday, lat) # instant of sunrise
    if dawn >= jday:
        ans = floor(jday)
    else:
        ans = ceil(jday)
    return ans

def fromjd(jday):
    '''Convert a Julian Day into a date in the True Hindu solar calendar'''
    jday = Fraction(jday) # Julian Day in question

    year = (jday - epoch) // sid_year
    sankranti = epoch + (year * sid_year) # approximate time the sun enters crosses Revati
    #print(float(sankranti))
    while suncheck(ntime(sankranti, 0)) > jday:
        sankranti -= sid_year
        year -= 1
    while suncheck(ntime(sankranti + sid_year, 0)) <= jday:
        sankranti += sid_year
        year += 1
    #m = (jday - sankranti) // rasi # month number
    #print(m)
    m = 0

    while suncheck(ntime(sankranti + (m * rasi), (m * 30))) > jday:
        m -= 1            
    while suncheck(ntime(sankranti + ((m + 1) * rasi), ((m + 1) * 30))) <= jday:
        m += 1
    #print(float(sankranti))
    #print(float(sunrise(sankranti, lat)))
    #print(m)


    month = NUMON[m]
    mu = suncheck(ntime(sankranti + (m * rasi), (m * 30)))
    day = jday - mu + 1

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a date in the True Hindu solar calendar into a Julian Day'''
    day = int(day)
    month = str(month)
    year = int(year)

    m = MONTHNO[month] # month number

    jday = epoch + (year * sid_year)
    jday = jday + (m * rasi)
    jday = suncheck(ntime(jday, (m * 30))) + day - 1

    return jday
