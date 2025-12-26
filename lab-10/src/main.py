# main.py

from modules.graph_representation import AdjacencyМatrix, AdjacencyList
from modules.graph_traversal import bfs, dfs_recursive, dfs_iterative
from modules.shortest_path import (
    topological_sort, connected_components, dijkstra,
    find_shortest_path_in_maze)
from modules.perfomance_analysis import Visualisation

matrix = AdjacencyМatrix(directed=False)
for _ in range(0, 6):
    matrix.add_vertex()

matrix.add_edge(2, 3)
matrix.add_edge(3, 1)
matrix.add_edge(4, 0)
matrix.add_edge(4, 1)
matrix.add_edge(5, 0, 99)
matrix.add_edge(5, 2)

# print("Topological Sort:", topological_sort(matrix))
print("BFS from vertex 5:", bfs(matrix, 5))
print("DFS Recursive from vertex 5:", dfs_recursive(matrix, 5))
print("DFS Iterative from vertex 5:", dfs_iterative(matrix, 5))

for i in connected_components(matrix):
    print("Connected Component:", i)

ways = dijkstra(matrix, 5)
for i in range(len(ways)):
    print(f"Shortest path from 5 to {i}: {ways[i]}")

Visualisation([100, 150, 200, 250, 300, 350, 400, 450, 500, 550,
              600, 650, 700, 750, 800, 850, 900, 950, 1000])

print("\nGraph Representation:\n")
print("Adjacency Matrix:")
matrix.print_matrix()
print("\nAdjacency List:")
lst = AdjacencyList()
lst.matrix_to_list(matrix)

lst.print_list()

print("Maze-task")
maze = AdjacencyМatrix(directed=False)
# 0 - road, 1 - wall
#  [s, 1, 0, 0, 0, e],
#  [0, 1, 0, 1, 1, 0],
#   [0, 0, 0, 0, 1, 0],
#   [0, 1, 1, 0, 1, 0],
#  [0, 0, 0, 0, 0, 0],
#

for _ in range(30):
    maze.add_vertex()

edges = [
    (0, 6), (6, 12), (12, 18), (18, 24), (24, 25),
    (12, 13), (13, 14), (25, 26), (14, 8), (14, 15),
    (8, 2), (2, 3), (3, 4), (4, 5), (26, 27), (27, 28),
    (28, 29), (14, 20), (5, 11), (11, 17), (17, 23), (23, 29)
]
for u, v in edges:
    maze.add_edge(u, v)

path = find_shortest_path_in_maze(maze, 0, 5)
print("Shortest path in maze from S(0) to E(5):", path)

# Характеристики вычислительной машины
pc_info = """
Характеристики ПК для тестирования:
- Процессор: Intel Core i5-11500H @ 2.50GHz
- Оперативная память: 8 GB DDR4
- ОС: Windows 11
- Python: 3.12
"""
print(pc_info)
