import sys

class Graph:
    def __init__(self, nodelist):
        self.nodes = {v.name:v for v in nodelist}

    def make_edge(self, id1, id2, weight):
        eg1 = self.nodes.get(id1)
        eg2 = self.nodes.get(id2)
        if eg1 is not None and eg2 is not None:
            eg1.add_adj(eg2.name, weight)
            eg2.add_adj(eg1.name, weight)
                
    def edges(self):
        edges = []
        for e in self.nodes.values():
            edges += list(e.adjs())
        return edges

class Node:
    def __init__(self, name):
        self.graph = None
        self.adj = {}
        self.name = name
        self.pi = None
        self.d = sys.maxsize

    def add_adj(self, id, weight):
        self.adj[id] = weight
    
    def remove_adj(self, id):
        try:
            del self.adj[id]
        except:
            pass
    
    def adjs(self):
        return list(self.adj.items())


def dijsktra(graph, src):

    visited = []
    source = graph.nodes[src]
    source.d = 0
    Q = list(graph.nodes.values())
    while len(Q):
        u = sorted(Q, key=lambda e: e.d)[0]
        Q.remove(u)
        visited.append(u)

        for v, weight in u.adjs():
            v = graph.nodes[v]
            if  v.d  >  u.d + weight:
                v.d =  u.d + weight
                v.pi = u

    for node in graph.nodes.values():
        if node.d != 0:
            yield node.d
    

N, M  = list(map(int, input().strip().split()))
g = Graph([Node(i) for i in range(1,N+1)])
for k in range(M):
    D,S,W = list(map(int, input().strip().split()))
    g.make_edge(D,S,W)
src = int(input().strip())
djk = list(dijsktra(g, src))
if len(djk) > 1:
    print(max(djk) - min(djk))
else:
    print(0)
   