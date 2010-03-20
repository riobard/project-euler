from __future__ import division

def fib(nth):
    '''
    Calculate the approximation of the n-th fibonacci number

    This is useful to get the most significant digits of the number, but is
    not accurate for the least significant digits
    '''
    phi = (1+5**.5)/2   # golden ratio
    return int((phi**nth + (1 - phi)**nth) / (5**.5))   # will overflow



'''
basic idea for the following code:

check the last 9 digits, if it is pandigital, then use the fib(nth) function
above to check the first 9 digits. when iterating the fib numbers, only add
the last 9 digits with modulo arithmetic. this will speed up because fewer 
big ints are used. 

In short, 
1) addition mod 10^9 to track the last 9 digits (iteration approach)
2) multiplication by (1+sqrt(5))/2 to track the first 9 digits (golden ratio)


from math import sqrt
 
def isPandigital(s):
    return set(s) == set('123456789')
 
rt5=sqrt(5)
def check_first_digits(n):
    def mypow( x, n ):
        res=1.0
        for i in xrange(n):
            res *= x
            # truncation to avoid overflow:
            if res>1E20: res*=1E-10
        return res
    # this is an approximation for large n:
    F = mypow( (1+rt5)/2, n )/rt5
    s = '%f' % F
    if isPandigital(s[:9]):
        print n
        return True
 
a, b, n = 1, 1, 1
while True:
    if isPandigital( str(a)[-9:] ):
        # Only when last digits are
        # pandigital check the first digits:
        if check_first_digits(n):
            break
    a, b = b, a+b
    b=b%1000000000
    n += 1

exit()
'''

'''
F(n) = n               # n <= 1
F(n) = F(n-1) + F(n-2) # n >  1
'''

a, b, k    = 0, 1, 0
d   = set('123456789')
while 1:
    if set(str(a%10**9)) == d == set(str(a)[:9]):
        print k
        break

    a, b    = b, a+b
    k       += 1
    if not (k % 1000):
        print k
