def old():
    ' old version of the problem solved using brutal force '
    n   = 10000//3
    d   = {}
    for a in range(1,n+1):
        for b in range(a+1, n+1):
            s   = a*a + b*b
            c   = int(s**.5)
            l   = a + b + c
            if l > 10000:
                break
            if (s == c*c):
                if l in d:
                    d[l]  += 1
                else:
                    d[l]  = 1

    print sum(d[k] == 1 for k in d)





    


def PPT(f, a=3, b=4, c=5):
    ' Primitive Pythagorean Triples '

    if f(a, b, c):
        PPT(f, a-2*b+2*c, 2*a-b+2*c, 2*a-2*b+3*c)
        PPT(f, a+2*b+2*c, 2*a+b+2*c, 2*a+2*b+3*c)
        PPT(f, -a+2*b+2*c, -2*a+b+2*c, -2*a+2*b+3*c)


M = 1500000
L = [0] * (M+1)

def f(a, b, c):
    l = a + b + c
    if l > M:
        return False    # discontinue recursion in PPT

    k = 0
    while True:
        k += 1
        kl = k * l  # PPT's can be scaled: (3, 4, 5) -> (30, 40, 50)
        if kl > M:
            break
        else:
            L[kl] += 1

    return True # continue recursion


PPT(f)

print sum(1 if L[i]==1 else 0 for i in xrange(M+1))
