from itertools import count


def find(M=10**12):
    sqrt2 = 2**.5
    t = M
    while True:
        T = t*(t-1)
        b = int(t/sqrt2)
        while True:
            B = 2*b*(b-1)
            if B==T:
                return b, t, B, T
            elif B > T:
                break
            else:
                b += 1

        t += 1


def test():
    ' use this to find the initial values of b '
    t = 2
    while True:
        b, t, B, T = find(t)
        print b, 
        t += 1




def A011900():
    ' http://oeis.org/A011900 '
    a = 1
    b = 3
    while True:
        yield a
        a, b = b, 6*b - a - 2


def brutalforce():
    ''' 
    b = # of blue discs; t = # of total discs 

    b(b-1)   1
    ------ = -
    t(t-1)   2

    since t >= 10^2 is quite huge, use approximation
    b^2   1
    --- = -
    t^2   2

    t >= 10^2, t^2 >= 10^24, therefore search for 2b^2 >= 10^24
    '''
    for b in A011900():
        if 2*b*b >= 10**24:
            return b



'''
Analytical method:

    b = # of blue discs
    t = # of total discs

    b(b-1)   1
    ------ = -
    t(t-1)   2

    2(b^2 - b) - (t^2 - t) = 0

    In general the way to solve these equations is to turn them into Pell's equation
    by linear substitution:

    2(b^2 - b - 1/4 + 1/4) - (t^2 - t - 1/4 + 1/4) = 0
    2((b-1/2)^2 + 1/4) - ((t-1/2)^2 + 1/4) = 0

    let x/2 = b-1/2
        y/2 = t-1/2

    2((x^2)/4 + 1/4) - ((y^2)/4 + 1/4) = 0
    2(x^2 + 1) - (y^2 + 1) = 0
    2x^2 - y^2 = 1

    Now use Pell's equation to solve x, y (see Problem 66)
'''
