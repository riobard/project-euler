class Graph(object):
    g   = {}    # {src: {neighbor: weight of edge src->neighbor}, ...}

    def __init__(self, iter=[]):
        for src, dst, weight in iter:
            self.add(src, dst, weight)
    
    def add(self, src, dst, weight):
        ''' Add an edge from src to dst with weight '''
        self.g.setdefault(src, {})[dst] = weight
    
    def neighbors(self, node):
        ''' Return a dict of {neighbor: weight} of all neighbors of node '''
        return self.g.get(node, {})

    def weight(self, src, dst):
        ''' Return the weight of the edge from src to dst '''
        return 0 if src==dst else self.g[src][dst]

DirectedGraph   = Graph     # DirectedGraph is an alias to Graph

class UndirectedGraph(Graph):
    def add(self, src, dst, weight):
        super(self.__class__, self).add(src, dst, weight)
        super(self.__class__, self).add(dst, src, weight)

def dijkstra(graph, src):
    ''' Generate the shortest path to each node from src
    
    Each time the generator will yield a tuple of (parent, child, cost),
    an edge of the shortest path spanning tree rooted from src in graph
    '''

    assert isinstance(graph, Graph)

    pending = set([src])
    closed  = set()
    mintc   = {src: 0}      # min total cost to each node from src
    parent  = {}            # {child: parent} track path to each node

    while pending:
        tc, cur = min((mintc[each], each) for each in pending)
        if cur in parent:   # skip the root node (with no parent) of the tree
            yield parent[cur], cur, graph.weight(parent[cur], cur)
        pending.remove(cur)
        closed.add(cur)

        for node in graph.neighbors(cur):
            if node not in closed:
                assert graph.weight(cur, node) >= 0
                # Dijkstra's algorithm only works for non-negative weight
                cost = mintc[cur] + graph.weight(cur, node)
                if node in pending:
                    if cost < mintc[node]:  # if a shorter path is found
                        mintc[node] = cost  # update cost and trace
                        parent[node]= cur
                else:
                    pending.add(node)
                    mintc[node] = cost
                    parent[node]= cur

def shortestPath(graph, src, dst):
    tree    = {}
    for parent, child, cost in dijkstra(graph, src):
        tree[child] = parent
        if child==dst: break

    def traceToRoot(tree, node):
        ''' Trace the path from node to root in tree '''
        yield node
        while node in tree:
            node    = tree[node]
            yield node

    return list(traceToRoot(tree, dst))[::-1] # reverse the path so src->dst



if __name__ == '__main__':
    g   = UndirectedGraph([
        ('O', 'A', 2),
        ('O', 'B', 5),
        ('O', 'C', 4),
        ('A', 'B', 2),
        ('C', 'B', 1),
        ('A', 'D', 7),
        ('B', 'D', 4),
        ('B', 'E', 3),
        ('C', 'E', 4),
        ('D', 'E', 1),
        ('D', 'T', 5),
        ('E', 'T', 7),
        ])

    for node in dijkstra(g, 'O'):
        print node

    print shortestPath(g, 'O', 'T')
