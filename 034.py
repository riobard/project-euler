'''
1   = 1!
2   = 2!
145 = 1! + 4! + 5! = 1 + 24 + 120
40585   = 4!+ 0! + 5! + 8! + 5! = 24 + 1 + 120 + 40320

These four numbers are called ``factorion'', a natural number that equals the
sum of the factorials of its decimal digits. These are the only four. 

To search for them, we need an upper bound. 

If n contains d digits, and it's a factorion, it must hold true that
    10^(d-1) <= n <= d * 9!
thus
    10^(d-1) <= d*9!
Note 10^(d-1) grows exponentially and d*9! grows linearly. when d >= 8, the
above inequation no longer holds true. Thus d must <= 7. So the upper bound to
check is 7*9! = 2540160. 
'''

from euler import factorial as f

def factorion():
    for i in range(7*f[9]):
        if i == sum(f[x] for x in map(int, str(i))):
            yield i

factorions  = list(factorion())
print factorions
print sum(factorions) - 1 - 2
