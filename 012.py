
def factor(n):
    return [x for x in range(1, n//2 + 1) if not (n % x)] + [n]


from euler import primefactors as factorize
print list(factorize(2**10))


for i in range(1, 10**2):
    fs  = list(factorize(i))
    ff  = factor(i)
    print len(ff),'\t', i,'\t', fs, '\t', ff
