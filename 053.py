'''
A much more efficient approach using Pascal Triangle

C(n, r) results the Pascal Triangle

0:       1
1:      1 1
2:     1 2 1
3:    1 3 3 1
4:  1 4  6  4 1
5: 1 5 10 10 5 1 

with n (from 0) denoting row and r (from 1) denoting column. 

Each row of this triangle is symmetric and bell-curve shaped, so C(n, r) ==
C(n, n-r) and any C(n, x) for x between r and (n-r) is greater than C(n, r). 

Thus if C(n, r) > 10**6, we know that C(n, x) for x from r to (n-r) must also
> 10**6. Total number of C(n, r) > 10**6 is (n-r)-r+1. So during looping we
stop whenever C(N, r) > 10**6 is encountered and try next row. This will
save the time needed to check all numbers in a given row. 
'''

from euler import combination as C

total   = 0
for i in range(0,101):
    for j in range(i+1):
        if C(i,j) > 10**6:
            total   += i-j-j+1
            break
print total
