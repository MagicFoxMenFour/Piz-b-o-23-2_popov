# graph_unittest.py

import unittest
from src.modules.graph_representation import AdjacencyМatrix
from src.modules.graph_traversal import bfs, dfs_recursive, dfs_iterative
from src.modules.shortest_path import (
    topological_sort, connected_components, dijkstra)


class TestGraphMethods(unittest.TestCase):
    def setUp(self):
        self.matrix = AdjacencyМatrix(directed=False)
        for _ in range(6):
            self.matrix.add_vertex()
        self.matrix.add_edge(2, 3)
        self.matrix.add_edge(3, 1)
        self.matrix.add_edge(4, 0)
        self.matrix.add_edge(4, 1)
        self.matrix.add_edge(5, 0, 99)
        self.matrix.add_edge(5, 2)

    def test_bfs(self):
        result = bfs(self.matrix, 5)
        self.assertEqual(result, [5, 0, 2, 4, 3, 1])

    def test_dfs_recursive(self):
        result = dfs_recursive(self.matrix, 5)
        self.assertEqual(result, [5, 0, 4, 1, 3, 2])

    def test_dfs_iterative(self):
        result = dfs_iterative(self.matrix, 5)
        self.assertEqual(result, [5, 0, 4, 1, 3, 2])

    def test_topological_sort(self):
        directed_matrix = AdjacencyМatrix(directed=True)
        for _ in range(6):
            directed_matrix.add_vertex()
        directed_matrix.add_edge(5, 2)
        directed_matrix.add_edge(5, 0)
        directed_matrix.add_edge(4, 0)
        directed_matrix.add_edge(4, 1)
        directed_matrix.add_edge(3, 1)
        directed_matrix.add_edge(2, 3)

        result = topological_sort(directed_matrix)
        self.assertEqual(result, [4, 5, 0, 2, 3, 1])

    def test_connected_components(self):
        result = connected_components(self.matrix)
        expected = [[0, 4, 1, 3, 2, 5]]
        self.assertEqual(len(result), len(expected))
        for comp in expected:
            self.assertIn(comp, result)

    def test_dijkstra(self):
        ways = dijkstra(self.matrix, 5)
        expected = [5, 3, 1, 2, 4, 0]
        self.assertEqual(list(ways.values()), expected)
