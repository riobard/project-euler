from utils import timex
from euler import pythagorean

timex()
for a,b,c in pythagorean(1000):
    if a+b+c==1000:
        print a*b*c
        break
timex()
