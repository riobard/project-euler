'''
http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion 

Related to P065, P066
'''

def CFE(s):
    ' Continued fraction expansion of sqrt(s) '

    m   = 0
    d   = 1
    a0  = int(s**.5)
    a   = a0
    
    encountered = set([(m, d, a)])
    rs  = [a0]

    while True:

        m   = d * a - m
        d   = (s - m**2) / d
        if d == 0: break    # a perfect square
        a   = int(a0 + m) // d

        if (m, d, a) in encountered:
            break
        else:
            rs  += [a]
            encountered.add((m, d, a))

    return rs


print sum(1 for n in range(10000+1) if len(CFE(n)) > 1 and len(CFE(n)) % 2==0) 
