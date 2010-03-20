def triple(ls):
    '''
    a special permutation

    ls  = [a, b, c, d, e]   # in asc order
    produce:
        abc abd abe acd ace ade
        bcd bce bde
        cde
    '''
    for i in range(len(ls)):
        for j in range(i+1, len(ls)):
            for k in range(j+1, len(ls)):
                yield [ls[i], ls[j], ls[k]]

from euler import primesieve, isarithmetic

s   = set(primesieve(10000)) - set(primesieve(1000))
d   = {}
for each in sorted(s):
    digits  = tuple(sorted(map(int,str(each))))
    if digits in d:
        d[digits].append(each)
    else:
        d[digits]   = [each]

for digits in sorted(d):
    if len(d[digits]) >= 3:
        for each in triple(d[digits]):
            if isarithmetic(each):
                print each
