from euler import prime
from itertools import takewhile


def run():
    MAX = 50000000

    p   = list(takewhile(lambda n: n <= MAX**.5, prime))
    p2  = [n**2 for n in p]
    p3  = [n**3 for n in p]
    p4  = [n**4 for n in p]

    s   = set()
    for a2 in p2:
        if a2 > MAX: break
        for b3 in p3:
            if a2 + b3 > MAX: break
            for c4 in p4:
                if a2 + b3 + c4 > MAX: break
                s.add(a2+b3+c4)     # remove duplicates in a set

    return len(s)


rs  = run()
print rs
assert 1097343 == rs

