'''
http://en.wikipedia.org/wiki/Continued_fraction
'''

def h():
    a   = 3
    b   = 7
    while True:
        yield a
        a, b    = b, 2*b + a


def k():
    a   = 2
    b   = 5
    while True:
        yield a
        a, b    = b, 2*b + a


from itertools import izip

cnt = 0
i   = 0
for (x, y) in izip(h(), k()):
    if i == 1000: break
    i   += 1
    if len(str(x)) > len(str(y)): cnt += 1

print cnt
