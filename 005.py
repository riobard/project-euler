''' the idea is simple: factorize every number from 1 to 20, that is to
reduece every number to its basic form (a unique form expessed using only
prime numbers, due to the fact that every natural number has a unique form).
and then find the maximum power of each prime element.  

1*2*3*(2*2)*5*(2*3)*7*(2*2*2)*(3*3)*(2*5)*11*(2*2*3)*13*(2*7)*(3*5)*(2*2*2*2)*17*(2*3*3)*19*(2*2*5)

1*(2**4)*(3**2)*5*7*11*13*17*19
'''

from euler import uniprimefact, product

nums    = range(1, 20)

d   = {}
for i in nums:
    for (prime, power) in uniprimefact(i).items():
        if (prime in d and d[prime] < power) or (prime not in d):
            d[prime]    = power 

print product(prime**power for (prime, power) in d.items())
