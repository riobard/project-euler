'''
P0018, P0067, P0081, P0083 are variants of each other. 

Dynamic Programming
    1) overlapping subproblems
    2) optimal substructure

Two approaches:
    1) Top-down: memoization
    2) Bottom-up: 
'''

mat = '''\
3
7 5
2 4 6
8 5 9 3\
'''

mat = '''\
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23\
'''

mat = [map(int, line.split()) for line in mat.split('\n')]
M   = len(mat)-1

from euler import memoized

@memoized
def f(i, j):
    if i==M:    return mat[i][j]
    else:       return mat[i][j] + max(f(i+1, j), f(i+1, j+1))

print f(0,0)
