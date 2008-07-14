def buildgraph(M):
    g   = {}    # graph as a dict of dicts of edge weights
    X   = len(M)
    Y   = len(M[0])
    for i in range(X):
        for j in range(Y):
            n   = {}    # neighbors to node (i, j)
            if i+1 < Y:
                n[(i+1, j)] = M[i+1][j]
            if j+1 < X:
                n[(i, j+1)] = M[i][j+1]
            if i > 0:
                n[(i-1, j)] = M[i-1][j]
            if j > 0:
                n[(i, j-1)] = M[i][j-1]
            g[(i,j)]    = n
    return g

def tracetosource(n, p):
    '''
    produce a path tracing back to source according to precedecssor p
    '''
    path    = []
    path.append(n)
    while n in p:
        n   = p[n]
        path.append(n)
    return path

def pathcost(p, g):
    '''
    return the cost of path p in graph g
    '''
    return 0 if len(p) < 2 else sum(g[a][b] for (a,b) in zip(p, p[1:]))


def dijkstra(g, s, d):
    '''
    Dijkstra's Shortest Path Algorithm

    Find the shortest path from source s to destination d in graph g

    Dijkastra is a special case of A* (A-star) path searching algorithm w/o
    heuristic (F = G + H, with H=0)

    A*: http://www.policyalmanac.org/games/aStarTutorial.htm
    '''
    open        = set([s])
    closed      = set()
    predecessor = {}
    cost        = {s:0}    # cost of path to node from s

    while open:
        mincost, current = min((cost[each], each) for each in open)
        open.remove(current)
        closed.add(current)
        if current==d:
            break
        for neighbor in g[current]:
            if neighbor in closed:
                continue
            if neighbor in open:
                newcost = cost[current] + g[current][neighbor]
                if newcost < cost[neighbor]:
                    predecessor[neighbor]   = current
                    cost[neighbor]          = newcost
            else:
                open.add(neighbor)
                predecessor[neighbor]   = current
                cost[neighbor]          = cost[current] + g[current][neighbor]

    return tracetosource(d, predecessor)[::-1] # reverse the traceback


M   = [[131, 673, 234, 103, 18],
        [201, 96, 342, 965, 150],
        [630, 803, 746, 422, 111],
        [537, 699, 497, 121, 956],
        [805, 732, 524, 37, 331]]
M = [map(int, line.strip().split(',')) for line in open('matrix.txt')]

N   = len(M)
g   = buildgraph(M)
g[(-1,-1)]  = {(0,0):M[0][0]}   # source outside the matrix

from time import clock
t   = clock()
path  = dijkstra(g, (-1,-1), (N-1, N-1))
print pathcost(path, g)
print clock() - t
