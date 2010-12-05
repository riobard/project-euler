from euler import gcd

def f(d):
    return sum(1 if 2*x < d < 3*x and gcd(x, d)==1 else 0
        for x in xrange(d//3, d//2+1))

print sum(f(d) for d in xrange(2, 12000+1))
