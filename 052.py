'''
After bruteforce: 

For this problem I didn't even use a computer. I just remembered that the repeating sequence of digits in the decimal representation of 1/7 has the desired property.

1/7 = 0.142857 142857 142857 ...

2 * 142857 = 285714
3 * 142857 = 428571
4 * 142857 = 571428
5 * 142857 = 714285
6 * 142857 = 857142
but
7 * 142857 = 999999 
'''

i   = 0
while True:
    i   += 1
    if set(str(i))==set(str(2*i))==set(str(3*i))==set(str(4*i))==set(str(5*i))==set(str(6*i)):
        print i
        break
