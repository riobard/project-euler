from __future__ import division

def tri(n):
    return n*(n+1)/2

def istri(n):
    i   = int((n*2) ** .5)
    return i*(i+1)/2 == n

def pen(n):
    return n*(3*n-1)/2

def ispen(n):
    i   = int(2/3 + (4/9 + 2*n/3)**.5)
    return  n==i*(3*i-1)/2

def hex(n):
    return n*(2*n-1)

i   = 143
while 1:
    i   += 1
    h   = hex(i)
    if istri(h) and ispen(h):   # in fact all Hex numbers are Tri numbers
        print h
        break
