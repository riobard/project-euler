def combo(xy, z):
    # xy = x + y 
    # 1 <= x <= y <= z
    # ===>
    # 1 <= x
    # xy - z <= x
    # x <= xy//2
    # x <= z
    # ===> max(1, xy-z) <= x <= min(xy//2, z)

    lo = max(1, xy-z)
    hi = min(xy//2, z)

    return hi - lo + 1 if lo <= hi else 0


def ncube(M):
    cnt = 0
    for z in xrange(1, M+1):
        for xy in xrange(2, 2*z + 1):
            xy2 = xy**2
            z2 = z**2
            k2 = xy2+z2
            k = int(k2**.5)
            if k**2 == k2:
                cnt += combo(xy, z)
    return cnt




def bisearch(f, cond, lo, hi):
    ''' 
    search a monotonously increasing function f for the first x s.t.
    cond(f(x)) is true and x is an integer and x >= 0
    '''

    while hi-lo > 1:
        x = (lo + hi) // 2
        n = f(x)
        if cond(n):
            hi = x
        else:
            lo = x

    return hi



def P086():
    assert 2060 == ncube(100)
    print bisearch(ncube, lambda n: n>1000000, 100, 10000)


P086()
