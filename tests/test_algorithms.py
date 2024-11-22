import unittest
from graph import Graph
from utils.errors import NodeNotFoundError

class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph(directed=True, weighted=True)

    def test_add_node(self):
        self.graph.add_node("A")
        self.assertIn("A", self.graph.nodes)

    def test_add_edge(self):
        self.graph.add_node("A")
        self.graph.add_node("B")
        self.graph.add_edge("A", "B", weight=2)
        self.assertIn(("A", "B", 2), self.graph.edges)

    def test_add_duplicate_node(self):
        self.graph.add_node("A")
        self.graph.add_node("A")
        self.assertEqual(len(self.graph.nodes), 1)

    def test_add_edge_between_nonexistent_nodes(self):
        with self.assertRaises(NodeNotFoundError):
            self.graph.add_edge("X", "Y", weight=2)

    def test_node_not_found(self):
        with self.assertRaises(NodeNotFoundError):
            self.graph.add_edge("X", "Y")

    def test_remove_node(self):
        self.graph.add_node("A")
        self.graph.remove_node("A")
        self.assertNotIn("A", self.graph.nodes)

    def test_remove_edge(self):
        self.graph.add_node("A")
        self.graph.add_node("B")
        self.graph.add_edge("A", "B", weight=2)
        self.graph.remove_edge("A", "B")
        self.assertNotIn(("A", "B", 2), self.graph.edges)

if __name__ == "__main__":
    unittest.main()