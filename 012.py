# for more information about this problem, check
# http://mathschallenge.net/index.php?section=faq&ref=number/number_of_divisors
#
# n can be uniquely represented by a^x * b^y * c^z, where a, b, c are primes
# let d(n) = the number of divisors of n
# then d(n) = (x+1) * (y+1) * (z+1)

from euler import primefactors, product
from itertools import count
from collections import defaultdict

def groupcount(sq):
    ''' Accept a sequence, sq, and count its elements by group '''
    d   = defaultdict(int)
    for each in sq:
        d[each] += 1
    return d

def trinum(n):
    ''' Return the n-th triangle number '''
    return n*(n+1)/2

def trinumgen():
    ''' Generate the sequence of triangle numbers '''
    for n in count(1):
        yield trinum(n)


for trin in trinumgen():
    primefs = primefactors(trin)
    if product(map(lambda x: x+1, groupcount(primefs).values())) > 500:
        print trin
        break
