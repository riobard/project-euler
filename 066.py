' Related to P064, P065 '

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


def convergent(CFE):
    
    def g(CFE):
        ' Generate a_i for i = 0, 1, 2, ... in the CFE '
        yield CFE[0]    # a0
        if len(CFE) > 1:
            while True:
                # square root has periodic CFE from a1 to an
                for each in CFE[1:]:    
                    yield each
    
    a = g(CFE)
    a0 = a.next()   # a0 will be the only element if CFE is from a square. 
    a1 = a.next()   # Throw StopIteration if CFE is not periodic and
                    # stop the outer generator as a side effect. Nice!

    hm, km = a0, 1
    kn, hn = a1, a0 * a1 + 1

    while True:
        yield (hn, kn)
        ai = a.next()
        hm, hn = hn, ai * hn + hm
        km, kn = kn, ai * kn + km



def pell(D):
    '''
    Pell's equation (http://en.wikipedia.org/wiki/Pell's_equation)

        x^2 - D * y^2 = 1

    if D is a square, there is no int solutions

    return the fundamental solution (x, y) s.t. x is minimal
    return None if no solution when D is a square
    '''

    for (x, y) in convergent(CFE(D)):
        if x**2 - D * y**2 == 1:
            return x, y


def P066(M):
    rs = []
    for D in xrange(1, M+1):
        xy = pell(D)
        if xy is not None:
            x, y = xy
            rs.append((x, D))

    return max(rs)[1]

print P066(1000)
