from utils import timex
from euler import ispalindromic

timex()
print max(i*j 
        for i in range(100,1000) 
        for j in range(100,1000) 
        if ispalindromic(str(i*j)))
timex()
