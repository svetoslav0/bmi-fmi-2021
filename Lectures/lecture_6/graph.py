import abc


class Graph(abc.ABC):

    def __init__(self, numVertices, directed=False):
        self.numVertices = numVertices
        self.directed = directed

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        pass

    @abc.abstractmethod
    def get_indegree(self, v):
        pass

    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        pass

    @abc.abstractmethod
    def display(self):
        pass


class Node:
    def __init__(self, vertexId):
        self.vertexId = vertexId
        self.adjacency_set = set()

    def add_edge(self, v):
        self.adjacency_set.add(v)

    def get_adjacent_vertices(self):
        return self.adjacency_set

    def __hash__(self):
        return hash(frozenset(self.vertexId))

    def __str__(self):
        return "id="+str(self.vertexId)

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False

        return (set(self.vertexId) == set(other.vertexId))


class AdjacencySetGraph(Graph):

    def __init__(self, numVertices, directed=False):
        super(AdjacencySetGraph, self).__init__(numVertices, directed)

        self.vertex_list = {}

    def add_edge(self, v1, v2, weight=1):
        if weight != 1:
            raise ValueError(
                "An adjacency set cannot represent edge weights >1")

        if not v1.vertexId in self.vertex_list:
            self.vertex_list[v1.vertexId] = v1

        self.vertex_list[v1.vertexId].add_edge(v2)
        if self.directed == False:
            if not v2.vertexId in self.vertex_list:
                self.vertex_list[v2.vertexId] = v2

            self.vertex_list[v2.vertexId].add_edge(v1)

    def get_adjacent_vertices(self, v):
        result = None
        if v.vertexId in self.vertex_list:
            result = self.vertex_list[v.vertexId].get_adjacent_vertices()

        return result

    def get_indegree(self, v):
        indegree = 0
        for i in self.vertex_list.keys():
            if v in self.get_adjacent_vertices(self.vertex_list[i]):
                indegree = indegree + 1

        return indegree

    def get_edge_weight(self, v1, v2):
        return 1

    def display(self):
        for i in self.vertex_list.keys():
            for v in self.get_adjacent_vertices(self.vertex_list[i]):
                print(self.vertex_list[i], "-->", v)
