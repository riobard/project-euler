# for more information about this problem, check
# http://mathschallenge.net/index.php?section=faq&ref=number/number_of_divisors
#
# According to Fundamental Theorem of Arithmetic (or Unique Prime-Factorization 
# theorem) <http://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic>,
# n can be uniquely represented by a^x * b^y * c^z, where a, b, c are primes
# let d(n) = the number of divisors of n
# then d(n) = (x+1) * (y+1) * (z+1)

from euler import uniprimefact, product
from itertools import count


def trinum(n):
    ''' Return the n-th triangle number '''
    return n*(n+1)/2

def trinumgen():
    ''' Generate the sequence of triangle numbers '''
    for n in count(1):
        yield trinum(n)

for trin in trinumgen():
    if product(each + 1 for each in uniprimefact(trin).values()) > 500:
        print trin
        break
