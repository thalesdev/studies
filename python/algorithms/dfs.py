import itertools
class Vertex:
    White = "#fff"
    Black = "#000"
    Gray = "gray" 
    def __init__(self, data, pi = None, d = 0, color= White, f = 0):
        self.data = data
        self.adj = []
        self.color = color
        self.pi = pi
        self.d = d
        self.f = f

    def add_edge(self, node):
        self.adj.append(node)
        return self
    def remove_edge(self, node):
        self.adj.remove(node)    
    def __iter__(self):
        return self.adj.__iter__()

    @staticmethod
    def generic_list(array): # Gera um gerador de vertex
        for data in array:
            yield Vertex(data)
        


class Graph:
    def __init__(self, list_vertex = [] ):
        self.vertex = list_vertex
    def __iter__(self):
        return self.vertex.__iter__()

# Variavel Global
time = 0
def DeepthFirstSearchVisit(vertex):
    # Visita os adjacentes ao vertex ate chegar no sumidouro
    global time
    time = time + 1
    vertex.d = time
    vertex.color = Vertex.Gray
    for vertexj in vertex:
        if vertexj.color == Vertex.White:
            vertexj.pi = vertex # seta o pai
            DeepthFirstSearchVisit(vertexj) # busca em profundidade nesse vertex
    vertex.color = Vertex.Black
    time = time+1
    vertex.f = time

def DeepthFirstSearch(graph, root):
    global time
    time = 0
    DeepthFirstSearchVisit(root) # Visita a raiz
    for vertex in list(set(graph).difference(root)): # Visita todos outros que nao sao a raiz
        if vertex.color == Vertex.White:
            DeepthFirstSearchVisit(vertex)

if __name__ == "__main__":
    # Cria o array com os vertex
    vertex =  list(Vertex.generic_list(["U","V","W","X", "Y", "Z"]))
    # Cria as relacoes
    vertex[0].add_edge(vertex[1]).add_edge(vertex[3])
    vertex[1].add_edge(vertex[4])
    vertex[2].add_edge(vertex[4]).add_edge(vertex[5])
    vertex[3].add_edge(vertex[1])
    vertex[4].add_edge(vertex[3])
    vertex[5].add_edge(vertex[5])
    # Cria o grafo
    grafo = Graph(vertex)
    # Chama o DFS
    DeepthFirstSearch(grafo, vertex[0])
    print("-- GRAFO -- Vertex:\n")
    # Printa o resultado
    for vertex in grafo:
        print("{}({}/{})".format(vertex.data,vertex.d, vertex.f))