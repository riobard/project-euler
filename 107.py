'''
Minimum Spanning Tree with Prim's Algorithm
'''

def buildmatrix(file):
    return [map(lambda s: None if s=='-' else int(s), line.strip().split(','))
            for line in open(file)]

def buildgraph(M):
    L   = len(M)
    g   = {}

    for i in range(L):
        neighbors   = {}
        for j in range(L):
            if M[i][j] is not None:
                neighbors[j]    = M[i][j]
        g[i] = neighbors

    return g

m   = buildmatrix('network.txt')
total   = sum(sum(each for each in line if each is not None) 
              for line in m) // 2 # symmetric weight matrix (undirected graph)
g   = buildgraph(m)
from euler import prim

mst = prim(g)
print total - sum(mst.values())
