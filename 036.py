from euler import ispalindromic, dec2bin

# this is slow (taking about 10 sec. to compute)
#print sum(i for i in range(10**6) if ispalindromic(str(i)) and
        #ispalindromic(dec2bin(i)))

'''
All palindromic numbers above 10 below 1,000,000 are in one of the following
forms:

AA
ABA
ABBA
ABCBA
ABCCBA

where A in [1,2,3,4,5,6,7,8,9], B and C in [0,1,2,3,4,5,6,7,8,9]. 

All single-digit numbers are palindromic numbers [0,1,2,3,4,5,6,7,8,9]. 

Notice that palindromic numbers are symmetric, so we only need to calculate the
first half of a palindromic number. 

If a palindromic number has n digits and n is even, it is in the same form of 
the palindromic number containing n-1 digits (n-1 is odd)---the only difference
is that it repeats the middle digit in the n-1 digit number. 

In base 2, all palindromic numbers must be odd, because if it is even, it must
ends with 0, while the first bit will never be 0. 
'''

def palindromicnumbers():
    '''
    Generate a list of all palindromic numbers containing up to 6 digits
    '''

    return map(int, ['%d' % (a)     # 10 1-digit numbers (including 0)
                for a in range(10)] +\
           ['%d%d' % (a,a)          # 9 2-digit numbers
                for a in range(1,10)] +\
           ['%d%d%d' % (a,b,a)      # 90 3-digit
                for a in range(1,10)
                for b in range(10)] +\
           ['%d%d%d%d' % (a,b,b,a)  # 90 4-digit, same as 3-digit
                for a in range(1,10)
                for b in range(10)] +\
           ['%d%d%d%d%d' % (a,b,c,b,a) # 900 5-digit
                for a in range(1,10)
                for b in range(10)
                for c in range(10)] +\
           ['%d%d%d%d%d%d' % (a,b,c,c,b,a) # 900 6-digit, same as 5-digit
                for a in range(1,10)
                for b in range(10)
                for c in range(10)])

# This is much more efficient
print sum(i for i in palindromicnumbers()
        if i%2 and ispalindromic(dec2bin(i)))

# now I'm going to write it like crazy Lisp-ist ...

def palindromic(n):
    '''
    Generate palindromic numbers containing n digits
    '''
    return range(10) if n==1 else map(int, ('%d'*n % (comb + comb[::-1][n%2:])
        for comb in reduce(lambda ts, es: [t+(e,) for t in ts for e in es], 
        [[(t,) for t in range(1,10)]] + [range(10)]*(sum(divmod(n,2))-1))))


print sum(each for each in reduce(lambda x,y: x+y,
    (palindromic(i) for i in range(1,7)))
    if each % 2 and ispalindromic(dec2bin(each)))

# eventually evolves into a one-liner ...

print sum(each for each in reduce(lambda x,y: x+y,  
    # this lambda for concatenating lists of palindromic numbers

    ((lambda n: range(10) if n==1 else map(int, 
    # this lambda for producing a list of palindromic numbers with n-digits

    ('%d'*n % (comb + comb[::-1][n%2:])
    # this is to expand (3,2,1) to (3,2,1,2,3) or (3,2,1,1,2,3), depending on
    # the required palindromic number containing odd/even number of digits,
    # thus the n%2 to test. comb[::-1] effectively reverses comb

    for comb in reduce(lambda ts, es: [t+(e,) for t in ts for e in es], 
    # this lambda for producing a list of tuple [(x,y) for x in xs for y in ys]
    # but it can do so for any number of 'for's!

    [[(t,) for t in range(1,10)]] + [range(10)]*(sum(divmod(n,2))-1))))
    # sum(divmod(n,2)) = n//2 + n%2. This is used to calculate half part of all
    # digits necessary to get the palindromic numbers
    # e.g.: AA = 1, ABA = 2, ABBA = 2, ABCBA = 3, ABCCBA = 3

    )(i) for i in range(1,7))) if each % 2 and ispalindromic(dec2bin(each)))
    # range(1,7) to produce palindromic numbers containing 1~6 digits
    # also check if the palindromic number is odd to speed up a little bit
