'''
P0018, P0067, P0081, P0082 are variants of each other. 

P0083 requires Graph Theory

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

mat = open('triangle.txt').read().strip()

mat = [map(int, line.split()) for line in mat.split('\n')]
M   = len(mat)-1

from euler import deepcopied
@deepcopied
def solve(l):
    for i in range(2,len(l)+1):
        for j in range(0,len(l[-i])):
            l[-i][j] += max(l[-i+1][j:j+2])
    return l[0][0]
print solve(mat)

from euler import memoized
@memoized
def f(i, j):
    if i==M:    return mat[i][j]
    else:       return mat[i][j] + max(f(i+1, j), f(i+1, j+1))

print f(0,0)
