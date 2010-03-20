from __future__ import division


'''
calculating the number to the left of 3/7 in each successive sequence ... 

This is Farey sequence:
F1  = 0/1, 1/1
F2  = 0/1, 1/2, 1/1
F3  = 0/1, 1/3, 1/2, 2/3, 1/1

Each term is the mediant of its neighbors. 
Mediant of a/b and c/d is (a+c)/(b+d)

See also Stern-Brocot Tree for a visual illustration of the process of
creating Farey sequence.  

So if we know a/b and c/d, the terms between them will be
a                a+c                 c
-                ---                 -
b                b+d                 d

a                a+c    a+2c         c
-                ---    ----         -
b                b+d    b+2d         d

a                a+c    a+2c  a+3c   c
-                ---    ----  ----   -
b                b+d    b+2d  b+3d   d

In general, the term immediately to the left of c/d will be (a+n*c)/(b+n*d). 

In this problem a=2, b=5, c=3, d=7. The term to the left of 3/7 is thus
    (2+3*n)/(5+7*n)

And 5+7*n <= 10**6, n == (10**6 - 5) // 7

The nominator would be (2 + 3 * ((10**6 - 5)//7))
'''

print (2 + 3 * ((10**6 - 5) // 7))

exit()

'''
The following code does the previous math iterally. 
'''

def prob71():
    a, b = 2, 5
    c, d = 3, 7
    for n in range(8, 10**6+1):
        m1, m2 = a + c, b + d
        if m2 <= n:
            a, b = m1, m2
    return a, b

print prob71()
exit()

'''
the following code works this way:
    1. List all n/d immediately to the left of 3/7 for d in [1,10**6]
    2. Remove k * (3/7)  (caused by Int conversion)
    3. Sort the result list in descending order
    4. Find the first fraction n/d such that hcf(n/d) == 1
'''

from euler import hcf


ds  = [(int(d*3/7), d) for d in range(1,10**6+1)]
ds.sort(key=lambda x: -x[0]/x[1])
ds  = [each for each in ds if each[0]/each[1] < 3/7]

for n,d in ds:
    if hcf(n,d) == 1:
        print '%d/%d = %10.10f' % (n, d, n/d)
        break

exit()

'''
L   = 3/7
min = L
min_= 0
for d in range(1,10**6+1):
    n   = int(d*L)
    if min > L - n/d != 0:
        min = L - n/d
        min_= d
print 'Done,', int(min_*L), '/', min_
'''

'''
Find the largest n/d such that
    1. n and d are positive integers
    2. n < d <= 10**6
    3. n/d < 3/7
    4. hcf(n, d) == 1

Procedures:
    1.  Check d from 10**6 to 1, since it is likely the largest n/d will be
        found when both n and d are large. 
    2.  For each d, check n from d*3/7 to 1, since n/d < 3/7 must hold true
    3.  Record the first pair of (n, d) such that hcf(n, d) == 1
    4.  Check next d
    5.  Repeat until d is 1
    6.  Compare pairs of (n, d) and find the largest n/d
'''

exit()  # this following code is fast to find the first two but slow to finish


p   = (0, 0, 0)
l   = 3/7
for d in range(10**6, 0, -1):
    for n in range(int(d*3/7), 1, -1):
        if hcf(n, d) == 1:
            k   = (n/d, n, d)
            if l > k[0] > p[0]:
                p   = k
                print '%d/%d = %10.10f' % (p[1], p[2], p[0])
            break
