from euler import properdivisors

def d(n):
    #return sum(x for x in range(1, n//2 + 1) if not (n % x))
    return sum(properdivisors(n))


s   = set()
for i in range(1,10000):
    m   = d(i)
    n   = d(m)
    if (i == n) and (m != n):
        s.add(m)
        s.add(n)

print s
print sum(s)
