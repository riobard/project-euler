''' 
Bruteforce approach:
    Permutate 0..9 and check if the number satisfies the constraints. 
    This needs 10! = 3628800 operations


A better approach:
    Since d2d3d4 is divisible by 2, d4 is even (0, 2, 4, 6, 8). 
    Since d4d5d6 is divisible by 5, d6 is 0 or 5. 
    Permutate remaining digits requires 8! operations. 
    This will reduce to 5 * 2 * 8! = 403200 operations


Further speedup:
    Since d8d9d10 is divisible by 17, d8d9d10 is multiples of 17 under 1000
    without redudant digits. There are 44 in total. 
    Permutate remainding digits.
    This will reduce to 5 * 2 * 44 * 5! = 52800 operations. 
'''

from euler import permutate, permutation as P

def unique(s):
    ''' check if a set has no redudant elements '''
    return len(s)==len(set(s))

def c8910():
    for each in range(17,1000,17):
        s   = map(int, '%03d' % each)
        if unique(s):
            yield s

def c4():
    for each in range(0,9,2):
        yield each

def c6():
    for each in (0,5):
        yield each

def c():
    digits  = set(range(10))
    for d4 in c4():
        for d6 in c6():
            for d8,d9,d10 in c8910():
                if unique([d4,d6,d8,d9,d10]):
                    for d1, d2, d3, d5, d7 in permutate(digits - 
                            set([d4,d6,d8,d9,d10])):
                        yield [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10]

def f():
    for n in c():
        if ((n[2]*100 + n[3]*10 + n[4]) % 3 == 0  and
            (n[4]*100 + n[5]*10 + n[6]) % 7 == 0  and
            (n[5]*100 + n[6]*10 + n[7]) % 11== 0  and
            (n[6]*100 + n[7]*10 + n[8]) % 13== 0):
            yield (n[9] + n[8]*10 + n[7]*10**2 + n[6]*10**3 +
                   n[5]*10**4 + n[4]*10**5 + n[3]*10**6 + 
                   n[2]*10**7 + n[1]*10**8 + n[0]*10**9)

print sum(list(f()))
