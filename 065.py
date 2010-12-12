'''
Variant of P057

http://en.wikipedia.org/wiki/Continued_fraction

e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...]


h_n = a_n * h_{n-1} + h_{n-2}

k_n = a_n * k_{n-1} + k_{n-2}


The first ten terms in the sequence of convergents for e are:

(h_n/k_n) = 2/1, 3/1, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536


Related to P064, P066

'''

from lazy import lazylist

@lazylist
def a():
    yield 2

    k = 1
    while True:
        yield 1
        yield 2*k
        yield 1
        k += 1
a = a()



@lazylist
def h():
    m = 2
    n = 3
    k = 2
    while True:
        yield m
        m, n = n, a[k] * n + m, 
        k += 1
h = h()


print sum(map(int, str(h[99])))
