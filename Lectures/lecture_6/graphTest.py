import unittest
from graph import *


class AdjacencySetGraphTest(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = AdjacencySetGraph(2)
        self.node1 = Node("test1")
        self.node2 = Node("test2")
        self.node3 = Node("test3")

    def test_add_edge_adjancent(self):
        self.graph.add_edge(self.node1, self.node2)

        adjacentNodes = self.graph.get_adjacent_vertices(self.node1)
        self.assertIsNotNone(adjacentNodes)
        self.assertEqual(self.node2, adjacentNodes.pop())

    def test_add_adge_not_direct_node2(self):
        self.graph.add_edge(self.node1,self.node2)
        self.assertIsNotNone(self.graph.get_adjacent_vertices(self.node2))

    def test_add_adge_not_direct_node1(self):
        self.graph.add_edge(self.node1,self.node2)
        self.assertIsNotNone(self.graph.get_adjacent_vertices(self.node1))

class AdjacencySetDirectedGraphTest(unittest.TestCase):

    def test_add_edge_wrong_error(self):
        graph = AdjacencySetGraph(2)
        node1 = Node("test1")

        with self.assertRaises(ValueError):
            graph.add_edge(node1, node1, 3)

    def test_add_adge_existing_node(self):
        graph = AdjacencySetGraph(2, True)
        node1 = Node("test1")
        node2 = Node("test2")

        graph.add_edge(node1,node2)
        self.assertIsNotNone(graph.get_adjacent_vertices(node1))

    def test_get_edge_weight(self):
         graph = AdjacencySetGraph(2, True)
         node1 = Node("test1")
         node2 = Node("test2")
         node3 = Node("test3")

         graph.add_edge(node1,node2)
         graph.add_edge(node2,node3)

         self.assertEqual(1, graph.get_edge_weight(node1, node3))

