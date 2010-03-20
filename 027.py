from euler import primesieve

'''
f(n)    = n*n + a*n + b

when n = 0, b must be a prime. And |b| < 1000, so b is one of the primes <
1000.
'''

primes  = set(primesieve(10**5))
def allprimes(n, a, b):
    ''' True if f(n, a, b) is prime for n in [0...n) '''
    ls  = [n*n + a*n + b for n in range(n)]
    largest = max(ls)

    if largest < 10**5:
        return all(l in primes for l in ls)
    else:
        raise Exception('Prime set not big enough. Max value %d' % largest)


from itertools import *
def mostprimes(a, b):
    ''' count how many primes for consecutive values of n '''
    for n in count():
        f   = n*n + a*n + b
        if f not in primes:
            break
    return n

prime1k = primesieve(1000)

# filter a to those produce at least 40 primes
als = [a for a in range(-999, 1000) for b in prime1k
       if allprimes(40, a, b)]

# leaving only this number of combinations of (a, b)
#print len(als) * len(prime1k)

rs  = max((mostprimes(a,b), a, b) for a in als for b in prime1k)
print rs[1]*rs[2]
