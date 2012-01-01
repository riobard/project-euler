from __future__ import division

from copy import deepcopy
def deepcopied(f):
    '''Deepcopy passed-in arguments to avoid side effects. '''
    return lambda *k: f(*(map(deepcopy, k)))

def memoized(f):
    '''Memoization decorator for referentially transparent function.'''
    m   = {}    # storage for key -> value pair
    l   = lambda *k: m[k] if k in m else m.setdefault(k, f(*k))
    l.cached    = m
    return l


def memoziedsequence(g):
    '''Decorate a generator and return a function that remembers its result.

    The generator produces a sequence which is cached and accessed by position.
    The decorated function is called to fetch cached results from previous
    calculation or call the generator to produce new result and cache it. 
    '''
    g, l   = g(), []
    def f(n):
    #def f(n, g=g(), l=[]):   # TRICK: mutable default value
        d   = n - len(l)    # position is 0-based indexed
        if d >= 0: l.extend(g.next() for _ in range(d+1))
        return l[n]
    return f

from lazy import lazylist

@lazylist
def fibonacci():
    '''Generate Fibonacci number sequentially.'''
    a, b    = 0, 1
    while True:
        yield a
        a, b    = b, a+b
fibonacci   = fibonacci()

@lazylist
def factorial():
    '''Generate factorial number sequentially.'''
    a, b    = 1, 1
    while True:
        yield a
        a, b    = a*b, b+1
factorial   = factorial()


def product(s):
    return reduce(lambda x,y:x*y, s, 1)

def ispalindromic(s):
    '''Check if a sequence is palindromic.
    
    A palindromic sequence reads the same both from left and right
    '''
    return all(s[i] == s[~i] for i in range(len(s)//2)) # ~0 == -1, ~1 == -2

def pythagorean(n):
    '''Generate Pythagorean triplet (a, b, c).
    
    such that 
    1) a < b < c <= n
    2) a**2 + b**2 == c**2
    '''
    for a in range(1,n+1):
        for b in range(a+1, n+1):
            s   = a**2 + b**2
            c   = int(s**.5)
            if (s == c**2) and (c <= n):
                yield (a,b,c)


@lazylist
def prime():
    '''Prime sequence generator.'''

    def hexstep():
        '''Generate 6n-1, 6n+1 sequence. '''
        n   = 1
        while True:
            hex = 6*n
            yield hex-1
            yield hex+1
            n   += 1

    def isprime(n):
        for p in primes:
            if n%p==0:  return False
            if p**2>n:  return True     # p**2>n is faster than p>n**.5

    yield 2
    yield 3
    primes  = [3]   # hexstep generates odd numbers, so 2 is unneccessary
                    # this list is interal cache of calcuated primes

    for n in hexstep():    # all primes (except 2 and 3) are 6n-1 or 6n+1
        if isprime(n):
            yield n
            primes.append(n)
prime   = prime()



def primefactors(n):
    '''Generate all prime factors of n.'''
    f = 2
    while f * f <= n:
        while not n % f:
            yield f
            n //= f
        f += 1
    if n > 1:
        yield n


def upf(n):
    'Unique prime factors of n'
    return set(primefactors(n))



def primefactors_slow(n):
    '''Generate all prime factors of n.'''
    for p in prime:
        if n > 1:
            while not (n % p):  # n can be evenly divided by prime p
                n   //= p
                yield p
        else:
            break


from utils import groupcount
def uniprimefact(n):
    ''' Return the Unique Prime-Factorization representation of n 
    
    let n = (a**x) * (b**y) * (c**z) * ...
    return {a: x, b: y, c: z, ...}
    '''

    return groupcount(primefactors(n))



def totient(n):
    ''' Euler's totient function: # of coprimes of n in [1, n) '''
    return product((p-1)*(p**(k-1)) for (p, k) in uniprimefact(n).items())


from math import sqrt

def primesieve(n):
    '''Sieve of Eratosthenes

    Return a list of all primes less than n
    '''
    l   = range(n)
    l[1]= 0
    for i in range(2, int(sqrt(n)) + 1):
        if l[i]:
            l[i**2::i]  = [0] * ((n - 1 - i**2)//i + 1)

    return [x for x in l if x]


def isprime(x):
    if x<5: return x==2 or x==3
    return x%2 and x%3 and all(x%(6*k-1) and x%(6*k+1)
            for k in range(1, int((x**.5 + 1)/6)+1))


def properdivisors(n):
    '''Generate a list of proper divisors of n

    If 2 is a PD of n, so is n/2. If 3 is a PD of n, so is n/3. Thus you only
    check until n**.5. 
    '''
    yield 1
    for i in xrange(2, int(n**.5)+1):
        if n % i == 0:
            yield i
            k   = n // i
            if i != k:
                yield k


def circulars(s):
    '''Generate circulars of sequence s

    eg. s = '123' => '123','231','312'
    '''
    return (s[i:] + s[:i] for i in range(len(s)))


def dec2bin(n):
    '''Return binary representation of decimal number n. '''
    s   = ''
    while n:
        s   = str(n%2) + s
        n >>= 1
    return s if s!='' else '0'

def permutate(s):
    '''Recursively generate all permutations of set s

    eg.
        s = [1,2,3]
    permutate(s) = [each element] + permutate(s without that element)
    '''
    s   = set(s)
    if s:
        for each in s:
            for rest in permutate(s - set([each])):
                yield [each] + rest
    else:
        yield []

def combinate(s, k):
    ''' Return k-combination from list s '''
    n   = len(s)
    #print 'k=%d, n=%d' % (k, n)
    if n == 0 or k == 0 or k > n:
        yield []
    else:
        assert 1 <= k <= n

        if k == 1:
            for each in s:
                yield [each]
        else:
            for i in range(n):
                each, others    = s[i], s[i+1:]
                for other in combinate(others, k-1):
                    if other != []:
                        yield [each] + other


def divisors(n):
    
    def decompose(n):
        for (prime, power) in uniprimefact(n).items():
            ls  = []
            for i in range(power+1):
                ls.append(prime**i)
            yield ls

    def vectorproduct(s1, s2):
        for e1 in s1:
            for e2 in s2:
                yield e1*e2

    def vectorloop(s):
        ts  = [1]
        for each in s:
            ts  = vectorproduct(ts, each)
        return ts

    def fnchain(a, fs):
        for f in fs:
            a  = f(a)
        return a

    return fnchain(n, [decompose, vectorloop, sorted])
    # == return sorted(vectorloop(decompose(n)))

def properdivisors2(n):
    # this is significantly slower than the previous method
    assert n > 1
    return divisors(n)[:-1]


def permutation(n, k):
    '''Number of permutations of k elements out of n elements.'''
    return factorial(n) // factorial(n - k)

def combination(n, k):
    '''Number of combinations of k elements out of n elements.'''
    return factorial(n) // (factorial(k) * factorial(n-k))


from itertools import imap, izip
def isarithmetic(s):
    '''Determine a sequence if it is an arithemtic sequence.

    An arithmetic sequence, [a, b, c, d] has constant difference between two
    consecutive elements
    '''
    if len(s) < 3:
        return False
    else:
        d       = s[1] - s[0]
        return all(imap(lambda (x,y): d==(y-x), izip(s, s[1:])))

def triplepermutate(ls):
    '''A special permutation

    ls  = [a, b, c, d, e]   # in asc order
    produce:
        abc abd abe acd ace ade
        bcd bce bde
        cde
    '''
    for i in range(len(ls)):
        for j in range(i+1, len(ls)):
            for k in range(j+1, len(ls)):
                yield [ls[i], ls[j], ls[k]]


def gcd(a, b):
    '''Return Greatest Common Divisor of a and b. '''
    while b:
        a,  b   = b, a % b
    return a
hcf = gcd   # gcd also known as Highest Common Factor

def lcm(a, b):
    '''Return the Least Common Multiple of a and b'''
    return a/gcd(a, b)*b    # (a*b)/gcd(a,b) => a/gcd(a,b)*b faster for big a,b

def ispandigital(n):
    '''Pandigital numbers contain all digits from 0 to 9'''
    return set(str(n)) == set('0123456789')


# Graph Theory

def dijkstra(g, s, d):
    '''Dijkstra's Shortest Path Algorithm. 

    Find the shortest path from source s to destination d in graph g

    Dijkastra is a special case of A* (A-star) path searching algorithm w/o
    heuristic (F = G + H, with H=0)

    A*: http://www.policyalmanac.org/games/aStarTutorial.htm

    Input:

        g: a graph as a dict of {node: {neighbor: weight, ...}, ...}
        s: source node
        d: destination node
    '''

    def tracetosource(n, p):
        '''
        produce a path tracing back to source according to precedecssor p
        '''
        path    = []
        path.append(n)
        while n in p:
            n   = p[n]
            path.append(n)
        return path

    open        = set([s])
    closed      = set()
    predecessor = {}
    cost        = {s:0}    # cost of path to node from s

    while open:
        mincost, current = min((cost[each], each) for each in open)
        open.remove(current)
        closed.add(current)
        if current==d:
            break
        for neighbor in g[current]:
            if neighbor in closed:
                continue
            if neighbor in open:
                newcost = cost[current] + g[current][neighbor]
                if newcost < cost[neighbor]:
                    predecessor[neighbor]   = current
                    cost[neighbor]          = newcost
            else:
                open.add(neighbor)
                predecessor[neighbor]   = current
                cost[neighbor]          = cost[current] + g[current][neighbor]

    return tracetosource(d, predecessor)[::-1] # reverse the traceback


def prim(g):
    '''Prim's Minimum Spanning Tree Algorithm.

    g: a graph as a dict of {node: {neighbor: weight, ...}, ...}

    (Only works for undirected graph, eg. for any i, j g[i][j] = g[j][i])
    '''
    solved  = set()
    mst     = set()
    edges   = set()

    current = g.keys()[0]   # choose arbitrary node to start
    while True:
        for neighbor in g[current]:
            edge    = (g[current][neighbor], frozenset([current, neighbor]))
            # use frozenset to store unorderd pair in set
            if edge in mst: continue
            edges.remove(edge) if edge in edges else edges.add(edge)

        if edges:
            edge    = min(edges)
            edges.remove(edge)
            mst.add(edge)

            _, (a, b) = edge
            solved.add(current)
            current = a if b in solved else b
        else:
            break

    return dict((pair, cost) for (cost,pair) in mst)    # set -> dict





def pentagonal(n):
    'Pentagonal number'
    return n*(3*n-1)/2



@memoized
def partition(n):
    '''
    # of ways to partition integer n
    
    Find the # of ways to partition a number

    http://www.math.temple.edu/~melkamu/html/partition.pdf

    p(<0) = 0 
    p(0) = 1
    p(n) = p(n-1) + p(n-2) - p(n-5) - p(n-7) + p(n-12) + p(n-15) - p(n-22) - p(n-26) + ...

    # of ways to partition n 
    p(n) = \sum_{k=1}^{\infinity} (-1)^(k+1) * { p(n-f(k)) + p(n-f(-k)) }

    '''

    if n < 0: 
        s   = 0
    elif n == 0:
        s   = 1
    else:
        s   = 0
        k   = 0
        while True:
            k   += 1
            sign= -1 if k%2==0 else 1
            m1  = n - pentagonal(k)
            m2  = n - pentagonal(-k)
            s   += sign * (partition(m1) + partition(m2))
            if m1 <= 0 or m2 <= 0:
                break

    return s


