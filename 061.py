from itertools import count
from euler import permutate

p3 = lambda n: n*(n+1)/2
p4 = lambda n: n*n
p5 = lambda n: n*(3*n-1)/2
p6 = lambda n: n*(2*n-1)
p7 = lambda n: n*(5*n-3)/2
p8 = lambda n: n*(3*n-2)


def take4digit(pn):
    for i in count(1):
        p = pn(i)
        if p < 1000:
            continue
        elif p > 9999:
            break
        else:
            yield p


p3s = tuple(take4digit(p3))
p4s = tuple(take4digit(p4))
p5s = tuple(take4digit(p5))
p6s = tuple(take4digit(p6))
p7s = tuple(take4digit(p7))
p8s = tuple(take4digit(p8))


def find(pa, pb, pc, pd, pe, pf):
    for a in pa:
        a34 = a%100
        for b in pb:
            if a34==b//100:
                b34 = b%100
                for c in pc:
                    if b34==c//100:
                        c34 = c%100
                        for d in pd:
                            if c34==d//100:
                                d34 = d%100
                                for e in pe:
                                    if d34==e//100:
                                        e34 = e%100
                                        for f in pf:
                                            if e34==f//100:
                                                f34 = f%100
                                                if f34==a//100:
                                                    return a,b,c,d,e,f

        

def tryall():
    ps = [p3s, p4s, p5s, p6s, p7s, p8s]
    for each in permutate(ps):
        rs = find(*each)
        if rs is not None:
            return rs

print sum(tryall())
