
'''
9-digit pandigitals are not prime, as 1+2+3+4+5+6+7+8+9=45 is divided by 3
8-digit pandigitals are not prime, as 1+2+3+4+5+6+7+8=36 is divided by 3
so check from 7-digit pandigitals
'''

from euler import isprime, permutate

digits  = range(7,0,-1)
for d in digits:
    for p in permutate(range(d,0,-1)):  # permutate in desc order
        n   = int(''.join(map(str,p)))
        #n   = sum(p[i]*(10**i) for i in range(len(p)))
        if isprime(n):
            print n
            break
