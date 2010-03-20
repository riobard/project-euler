'''
P0018, P0067, P0081, P0083 are variants of each other. 

Dynamic Programming
    1) overlapping subproblems
    2) optimal substructure

Two approaches:
    1) Top-down: memoization
    2) Bottom-up: 
'''

mat = [[131, 673, 234, 103,  18],
       [201,  96, 342, 965, 150],
       [630, 803, 746, 422, 111],
       [537, 699, 497, 121, 956],
       [805, 732, 524,  37, 331]]

mat = [map(int, line.strip().split(',')) for line in open('matrix.txt')]
M   = len(mat)-1

from euler import memoized

@memoized
def f(i, j):
    if i==j==M: return mat[i][j]
    elif i==M:  return mat[i][j] + f(i, j+1)
    elif j==M:  return mat[i][j] + f(i+1, j)
    else:       return mat[i][j] + min(f(i+1, j), f(i, j+1))

print f(0,0)
