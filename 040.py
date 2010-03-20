from euler import product

s   = '.' + ''.join((str(x) for x in range(1,10**6)))
print product(int(s[10**d]) for d in range(7))
