import unittest
from graphNode import Node

class NodeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.node = Node("test1")
    
    def test_add_edge(self):
        testNode = Node("test2")
        self.node.add_adge(testNode)

        adjacent_vertices = self.node.get_adjacent_vertices()
        self.assertIsNotNone(adjacent_vertices)
        self.assertIn(testNode, adjacent_vertices)

