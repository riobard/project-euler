def prim(g):
    '''
    Prim's Minimum Spanning Tree Algorithm

    (Only works for undirected graph)
    '''

    solved  = set([g.keys()[0]])    # get an arbitrary node from the graph
    remain  = set(g) - solved
    mst     = {}

    while remain:
        cost, last, next = min((g[last][next], last, next)
                for last in solved for next in g[last]
                if next not in solved)
        mst[(last, next)]   = cost
        solved.add(next)
        remain.remove(next)

    return mst


def buildmatrix(file):
    return [map(lambda s: None if s=='-' else int(s), line.strip().split(','))
            for line in open(file)]

def buildgraph(M):
    X   = len(M)
    Y   = len(M[0])
    g   = {}

    for i in range(X):
        neighbors   = {}
        for j in range(Y):
            if M[i][j] is not None:
                neighbors[j]    = M[i][j]
        g[i] = neighbors

    return g

from time import clock
m   = buildmatrix('network.txt')
total   = sum(sum(each for each in line if each is not None) 
              for line in m) // 2 # symmetric weight matrix (undirected graph)
g   = buildgraph(m)

t   = clock()
for i in range(1):
    mst = prim(g)
print clock() - t

print len(mst)
print sum(mst.values())
print total - sum(mst.values())




M   = [map(int, line.strip().split(',')) for line in open('matrix.txt')]
X   = len(M)
Y   = len(M[0])

g   = {}
for i in range(X):
    for j in range(Y):
        n   = {}
        if i+1 < Y:
            n[(i+1, j)] = M[i+1][j]
        if j+1 < X:
            n[(i, j+1)] = M[i][j+1]
        g[(i,j)]    = n

g[(X-1, Y-1)]   = {(0,0): M[0][0]}
g[(0,0)][(X-1,Y-1)] = M[0][0]
t   = clock()
mst = prim(g)
print clock() - t
