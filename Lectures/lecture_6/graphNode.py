
class Node:
    def __init__(self, vertexId) -> None:
        self.vertexId = vertexId
        self.adjacent = set()
        pass

    def add_adge(self, node):
        self.adjacent.add(node)
        pass

    def get_adjacent_vertices(self):
        return self.adjacent

    def __str__(self) -> str:
        return "vertexId=" + self.vertexId
    pass
