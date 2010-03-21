from euler import prime


'''
According to http://en.wikipedia.org/wiki/Euler's_totient_function

phi(n) = n * product( (1 - 1/p) for distinct prime p dividing n)

=> n/phi(n) = product( (1 - 1/p) for distinct prime p dividing n)

Since (1 - 1/p) < 1, to get the smaller n/phi(n), you just need as many
distinct prime as possible, as long as the product(p) <= 10**6

Hence it's trivial even on paper to find that: 

2 x 3 x 5 x 7 x 11 x 13 x 17 = 510510 <= 10**6

(the next number 510510 x 19 > 10**6)
'''


n   = 1
for p in prime:
    t   = n*p
    if t > 10**6:
        break
    else:
        n   = n * p

print n
