'''
This problem is a variant of P0076

'''

from euler import partition as p


n    = 0
while True:
    n   += 1
    pn  = p(n)

    if pn%1000000==0:
        break

print n, pn
