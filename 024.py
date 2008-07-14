'''
This has something to do with factoradic, a factorial-based mixed radix
numeral system

clever way by euler:

We know that there are n! permutations for n distinct digits and, as we're
working in lexicographical order, after 9! permutations the ten digit string
will have become: 0987654321. The 9!+1 permutation will be 1023456789, the
2*9!+1=725761 permutation will be 2013456789. However, the 3*9!+1 permutation
(3012456789) will be greater than one million. So we now consider the
permutations of the last nine digits, 013456789: 6*8!+1 will take it to
701345689. We have now computed 967681 permutations and arrived at the number
2701345689. Then we look at the last eight digits, and work out that a further
6*7!+1 takes it to the string 2780134569 and a total of 997921 permutations...

This method converges quickly.
'''

from euler import permutate as P, factorial as F

d   = '0123456789'
n   = 999999  # 0-based index of 1000000th permutation
ls  = ''
for i in range(9, -1, -1):
    q, n= divmod(n, F[i])
    print q,n,d
    ls  += d[q]
    d  = d[:q] + d[q+1:]

print ls
