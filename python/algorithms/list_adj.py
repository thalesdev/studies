import itertools as it


class Node:

    def __init__(self, data):
        self.__list_adjacent = []
        self.__data = data
        self.__degree = {
            "out": 0,
            "in": 0,
            "inout": 0
        }

    def adjacent(self):
        return self.__list_adjacent

    def append(self, node):
        self.__list_adjacent.append(node)

    def remove(self, node):
        self.__list_adjacent.remove(node)

    def __str__(self):
        return "<{}>".format(self.__data)

    def degree(self):
        return self.__degree


class Fork:
    def __init__(self, dirct=True):
        self.__nodes = []
        self.__directional = dirct

    def extend(self, list_nodes):
        self.__nodes.extend(list_nodes)

    def append(self, node):
        self.__nodes.append(node)
    
    def getNode(self, node_index):
        return self.__nodes[node_index]

    def remove(self, index):
        for node in self.__nodes:
            if self.__nodes[index] in node.adjacent():
                node.adjacent().remove(self.__nodes[index])
        self.__nodes.remove(self.__nodes[index])  # Fix

    def addEdge(self, source_node, dest_node):
        self.__nodes[source_node].append(self.__nodes[dest_node])
        if not self.__directional:
            self.__nodes[dest_node].append(self.__nodes[source_node])
            self.__nodes[source_node].degree()["inout"] += 1
            self.__nodes[dest_node].degree()["inout"] += 1
        else:
            self.__nodes[source_node].degree()["out"] += 1
            self.__nodes[dest_node].degree()["in"] += 1

    def removeEdge(self,  source_node, dest_node):
        self.__nodes[source_node].remove(self.__nodes[dest_node])
        if not self.__directional:
            self.__nodes[dest_node].remove(self.__nodes[source_node])

    def __iter__(self):
        return it.chain.from_iterable(self.__nodes)

    def __str__(self):
        str_ = ""
        for node in self.__nodes:
            pairs = []
            for friendly_node in node.adjacent():
                pairs.append(
                    "\n(" + str(node) + "," + str(friendly_node) + ")")
            str_ += "".join(pairs)
        return str_

    def sources(self):
        for node in self.__nodes:
            degree = node.degree()
            if degree["in"] == 0 and degree["out"] > 0:
                yield node

    def sinks(self):
        for node in self.__nodes:
            degree = node.degree()
            if degree["in"] > 0 and degree["out"] == 0:
                yield node


if __name__ == "__main__":

    grafo = Fork(dirct=True)
    grafo.extend([Node(data="A"), Node(data="B"), Node(
        data="E"), Node(data="D"), Node(data="F")])
    grafo.addEdge(0, 1)
    grafo.addEdge(3, 0)
    grafo.addEdge(3, 1)
    grafo.addEdge(3, 3)
    grafo.addEdge(4, 1)
    print("\naddEdge(0, 1);addEdge(3, 0);addEdge(3, 1);addEdge(3, 3);grafo.addEdge(4, 1);\n ", grafo)
    print("\nsources();\n", ",".join(list(map(str, grafo.sources()))))
    print("\nsinks();\n", ",".join(list(map(str, grafo.sinks()))))
    grafo.removeEdge(3, 0)
    print("\nremoveEdge(3, 0);\n", grafo)
    grafo.remove(3)
    print("\nremove(3);\n", grafo)
    print("\nsources();\n", ",".join(list(map(str, grafo.sources()))))
    print("\nsinks();\n", ",".join(list(map(str, grafo.sinks()))))
