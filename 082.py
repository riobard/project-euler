'''
P0018, P0067, P0081, P0082, P0083 are variants of each other. 

Dynamic Programming
    1) overlapping subproblems
    2) optimal substructure

Two approaches:
    1) Top-down: memoization
    2) Bottom-up: 
'''

mat = [[131,673,234,103,18],
       [201,96,342,965,150],
       [630,803,746,422,111],
       [537,699,497,121,956],
       [805,732,524,37,331]]

mat = [map(int, line.strip().split(',')) for line in open('matrix.txt')]
M   = len(mat) - 1

from euler import memoized
@memoized
def f(i, j, ii, jj=None):
    v   = mat[i][j]
    if j==M:
        return v
    elif i==0:
        if i==ii:
            return v + min(f(i, j+1, i), f(i+1, j, i))
        else:
            return v + f(i, j+1, i)
    elif i==M:
        if i==ii:
            return v + min(f(i, j+1, i), f(i-1, j, i))
        else:
            return v + f(i, j+1, i)
    else:
        if i < ii:
            return v + min(f(i-1, j, i), f(i, j+1, i))
        elif i > ii:
            return v + min(f(i+1, j, i), f(i, j+1, i))
        else:
            return v + min(f(i+1, j, i), f(i-1, j, i), f(i, j+1, i))

print min(f(i, 0, i) for i in range(M+1))
