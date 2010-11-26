'''
for all a >= 10, a^n will have at least n+1 digits

only need to check for a from 1 to 9



to calcuate the number of digits in an integer a**n

len(a**n)  = floor(log10(a**n)+1)

we want len(a**n) == n, so

log10(a**n) + 1 = n
log10(a**n) = n - 1
n * log10(a) = n - 1
log10(a) = 1 - 1.0/n


f(n) = 1 - 1.0/n increases as n grows
find the maximum n s.t.
log10(a) <= 1 - 1.0/n
'''

from math import log10

cnt = 0
for a in range(1, 10):
    log10a  = log10(a)
    n       = 0
    while True:
        n   += 1
        if (1 - 1.0/n) > log10a:
            cnt += n-1
            break

print cnt
