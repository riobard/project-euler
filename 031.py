'''
    5   2   1
-------------
10  2   0   0
10  1   2   1
10  1   1   3
10  1   0   5
10  0   5   0
10  0   4   2
10  0   3   4
10  0   2   6
10  0   1   8
10  0   0   10
--------------
'''


def f(n, us):
    '''
    Recursively generate all possible combinations of coins

    us must in desc order and the last element must be 1
    '''
    u, us   = us[0], us[1:]
    return [[n]] if u == 1 else [[i] + j
            for i in range(n//u, -1, -1) for j in f(n - i*u, us)]


print len(f(200, [200,100,50,20,10,5,2,1]))
