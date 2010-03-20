from __future__ import division
from euler import isprime
from itertools import izip


# helper functions
def take(n, iter):
    return [iter.next() for i in range(n)]

def count(offset=0, step=1):
    while True:
        yield offset
        offset   += step

# version 1, very slow
'''
def g():
    ' generate the # of elements in each circle of a spiral '
    last    = 0
    accu    = 0
    for each in (n**2 for n in count(1, 2)):
        last    = each - accu
        yield last
        accu    = each

def g2():
    cnt = count(1)
    for circle in (take(n, cnt) for n in g()):
        for each in circle[::-1][::max(1, len(circle)//4)][::-1]:
            yield each

def g3():
    ntotal      = 0
    nprimes     = 0
    for each in g2():
        ntotal  += 1
        if isprime(each):   nprimes += 1

        yield nprimes/ntotal

gg  = g3()
take(10, gg)    # initially is 0 because 1 is not prime
for (num, ratio) in izip(count(10), gg):
    #print num, '%3.2f' % ratio
    if ratio < 0.13: break
print 'Length', (num-1)//4 * 2 + 1
'''

# version 2, slightly better
'''
def g4():
    i   = 1
    l   = 3
    for n in count(8, 8):
        yield l, n, n+i
        i   += n
        l   += 2

def g5():
    for l,n,e in g4():
        for i in reversed(range(4)):
            yield e - i*(l-1)

ntotal  = 0
nprime  = 0
for each in g5():
    ntotal  += 1
    if isprime(each): nprime += 1
    if nprime/ntotal < .1: break
print int(each**.5)
'''

def g6():
    ' generate corner values of the spiral (excluding the center) '
    for i in count(3, 2):   # start from the 2nd circle (width=3)
        end = i**2          # the end value of the circle
        for j in reversed(range(4)):    # 4 corners of the circle
            yield end - j*(i-1)

def f(ratio):
    ntotal  = 0
    nprime  = 0
    for each in g6():
        ntotal  += 1
        if isprime(each):           nprime += 1
        if nprime/ntotal < ratio:   return int(each**.5)

print f(.1)
