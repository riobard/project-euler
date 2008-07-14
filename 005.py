''' the idea is simple: factorize every number from 1 to 20, that is to
reduece every number to its basic form (a unique form expessed using only
prime numbers, due to the fact that every natural number has a unique form).
and then find the maximum power of each prime element.  

1*2*3*(2*2)*5*(2*3)*7*(2*2*2)*(3*3)*(2*5)*11*(2*2*3)*13*(2*7)*(3*5)*(2*2*2*2)*17*(2*3*3)*19*(2*2*5)

1*(2**4)*(3**2)*5*7*11*13*17*19
'''

from euler import primefactors, product
from lazy import compact

frequent    = {}
for i in range(1,21):
    for (primefactor,cnt) in compact(primefactors(i)):
        if primefactor in frequent:
            if frequent[primefactor] < cnt:
                frequent[primefactor]   = cnt
        else:
            frequent[primefactor]   = cnt

print product(primefactor**cnt for (primefactor, cnt) in frequent.items())


# I don't know why the following works, but it's FAST!
# I guess the following code must be a watered-down version of the above
k = 1
for i in range(1, 21):
    if k % i:
        for j in range(1, 21):
            if not ((k*j) % i):
                k *= j
                break
print k
