'''
# This is gonna take a while
m, mm   = 1, 0
for n in range(2,10**6):
    k   = n
    i   = 1
    while n != 1:
        n   = 3*n + 1 if n % 2 else n/2
        i   += 1
    if i > m:
        m   = i
        mm  = k

print mm, m
'''

from utils import timex

d   = {1: 1}
def nterms(n):
    return d[n] if n in d else d.setdefault(n, 
            1 + (nterms(3*n+1) if n%2 else nterms(n/2)))

timex()
print max((nterms(n),n) for n in range(2,10**6))[1]
timex()
