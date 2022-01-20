from enum import Enum


class EdgeType(Enum):
    directed = 1
    undirected = 2


class Vertex:
    def __init__(self, data, index=None):
        self.data = data
        self.index = index


class Edge:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


class Graph:
    def __init__(self):
        self.adjacencies = {}

    def create_vertex(self, data):
        vertex = Vertex(data)
        self.adjacencies[vertex.data] = []

    def add_directed_edge(self, source, destination):
        self.adjacencies[source].append(destination)

    def add_undirected_edge(self, source, destination):
        self.adjacencies[source].append(destination)
        self.adjacencies[destination].append(source)

    def add(self, edge, source, destination):
        if edge == 1:
            self.add_directed_edge(source, destination)
        elif edge == 2:
            self.add_undirected_edge(source, destination)

    def dft(self, v, visited):
        visited.append(v)
        print(v, end=', ')
        for i in self.adjacencies[v]:
            if i not in visited:
                self.dft(i, visited)

    def friend_path(self, f0, f1):
        queue = []
        queue.append([f0])
        while queue:
            p = queue.pop(0)
            for n in self.adjacencies[p[-1]]:
                np = [p]
                np.append(n)
                queue.append(np)
                if n is f1:
                    return np


graph = Graph()
graph.create_vertex("VI")
graph.create_vertex("RU")
graph.create_vertex("PA")
graph.create_vertex("CO")
graph.create_vertex("CH")
graph.create_vertex("RA")
graph.create_vertex("KE")
graph.create_vertex("SU")
graph.add_undirected_edge("VI", "CH")
graph.add_undirected_edge("VI", "RU")
graph.add_undirected_edge("VI", "PA")
graph.add_undirected_edge("RU", "RA")
graph.add_undirected_edge("RU", "SU")
graph.add_undirected_edge("RU", "VI")
graph.add_undirected_edge("PA", "CO")
graph.add_undirected_edge("PA", "KE")
graph.add_undirected_edge("CO", "RU")
graph.add_undirected_edge("CO", "VI")
print(graph.friend_path("RU", "KE"))
