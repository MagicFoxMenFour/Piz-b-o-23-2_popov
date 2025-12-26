# shortest_path.py

# from src.modules.graph_traversal import dfs_recursive # tests
from modules.graph_traversal import dfs_recursive
import heapq
from collections import deque
# Топологическая сортировка: для ориентированных ациклических графов (DAG)


def topological_sort(graph):
    """
    Выполняет топологическую сортировку на
    ориентированном ациклическом графе (DAG),
    представленном матрицей смежности.
    Args:
        graph (AdjacencyМatrix): Граф, представленный матрицей смежности.
    Returns:
        list: Топологически отсортированный порядок вершин.
    """

    in_degree = [0] * len(graph.matrix)
    for u in range(len(graph.matrix)):
        for v in range(len(graph.matrix)):
            if graph.matrix[u][v] == 1:
                in_degree[v] += 1

    queue = deque([i for i in range(len(graph.matrix)) if in_degree[i] == 0])
    topo_order = []

    while queue:
        vertex = queue.popleft()
        topo_order.append(vertex)

        for neighbor in range(len(graph.matrix)):
            if graph.matrix[vertex][neighbor] == 1:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

    if len(topo_order) != len(graph.matrix):
        raise ValueError("Graph is not a DAG; topological sort not possible.")

    return topo_order
# Время: O(V + E)


# Поиск компонент связности


def connected_components(graph):
    """
    Находит все компоненты связности в неориентированном графе,
    представленном матрицей смежности.
    Args:
        graph (AdjacencyМatrix): Граф, представленный матрицей смежности.
    Returns:
        list of list: Список компонент связности, каждая из
        которых представлена списком вершин.
    """
    visited = set()
    components = []

    while len(visited) < len(graph.matrix):
        for i in range(len(graph.matrix)):
            if i not in visited:
                component = dfs_recursive(graph, i)
                for i in component:
                    visited.add(i)
                components.append(component)

    return components
# Время: O(V + E)

# Алгоритм Дейкстры для взвешенных графов


def dijkstra(graph, start):
    """
    Выполняет алгоритм Дейкстры для поиска
    кратчайших путей от стартовой вершины
    до всех остальных вершин в взвешенном графе,
    представленном матрицей смежности.
    Args:
        graph (AdjacencyМatrix): Взвешенный граф,
        представленный матрицей смежности.
        start (int): Начальная вершина.
    Returns:
        dict: Словарь с кратчайшими расстояниями от
        стартовой вершины до каждой вершины.
    """

    distances = {i: float('inf') for i in range(len(graph.matrix))}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor in range(len(graph.matrix)):
            weight = graph.matrix[current_vertex][neighbor]
            if weight > 0:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

    return distances
# Время: O((V + E) log V)


def find_shortest_path_in_maze(graph, start, end):
    """
    Находит кратчайший путь в лабиринте,
    представленном матрицей смежности.
    Args:
        graph (AdjacencyМatrix): Граф-лабиринт,
        представленный матрицей смежности.
        start (int): Начальная вершина.
        end (int): Конечная вершина.
    Returns:
        list: Список вершин, представляющих кратчайший путь
        от стартовой до конечной вершины.
    """
    distances = {i: float('inf') for i in range(len(graph.matrix))}
    previous = {i: None for i in range(len(graph.matrix))}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor in range(len(graph.matrix)):
            weight = graph.matrix[current_vertex][neighbor]
            if weight > 0:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))

    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()

    if distances[end] == float('inf'):
        return []  # Путь не найден

    return path
