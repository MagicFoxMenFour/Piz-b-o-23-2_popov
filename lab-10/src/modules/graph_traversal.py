# graph_traversal.py


# Поиск в ширину (BFS): находит кратчайшие
# пути в невзвешенном графе, сложность O(V + E)


def bfs(graph, start):
    """
    Выполняет поиск в ширину (BFS) на графе, представленном матрицей смежности.
    Args:
        graph (AdjacencyМatrix): Граф, представленный матрицей смежности.
        start (int): Начальная вершина для обхода.
    Returns:
        list: Порядок посещения вершин.
    """
    visited = set()
    queue = [start]
    order = []

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)
            neighbors = [
                idx for idx, val in enumerate(graph.matrix[vertex]) if val != 0
            ]
            queue.extend(neighbors)

    return order
# Время: O(V + E)

# Поиск в глубину (DFS): обход с возвратом, сложность O(V + E)


def dfs_recursive(graph, vertex, visited=None, order=None):
    """
    Выполняет рекурсивный поиск в глубину (DFS) 
    на графе, представленном матрицей смежности.
    Args:
        graph (AdjacencyМatrix): Граф, представленный матрицей смежности.
        vertex (int): Текущая вершина для обхода.
        visited (set): Множество посещенных вершин.
        order (list): Порядок посещения вершин.
    Returns:
        list: Порядок посещения вершин.
    """
    if visited is None:
        visited = set()
    if order is None:
        order = []

    visited.add(vertex)
    order.append(vertex)

    neighbors = [
        idx for idx, val in enumerate(graph.matrix[vertex]) if val != 0
    ]
    for neighbor in neighbors:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, order)

    return order
# Время: O(V + E)


def dfs_iterative(graph, start):
    """
    Выполняет итеративный поиск в глубину (DFS) 
    на графе, представленном матрицей смежности.
    Args:
        graph (AdjacencyМatrix): Граф, представленный матрицей смежности.
        start (int): Начальная вершина для обхода.
    Returns:
        list: Порядок посещения вершин.
    """
    visited = set()
    stack = [start]
    order = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)
            neighbors = [
                idx for idx, val in enumerate(graph.matrix[vertex]) if val != 0
            ]
            stack.extend(reversed(neighbors))

    return order
# Время: O(V + E)
