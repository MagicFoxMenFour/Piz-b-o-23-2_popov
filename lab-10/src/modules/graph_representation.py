# graph_representation.py

class AdjacencyМatrix:
    """
    Класс сущности матрицы смежности для представления графа.
    Attributes:
        matrix (list of list of int): Матрица смежности графа.
        directed (bool): Флаг, указывающий, является ли граф ориентированным.
    Память: O(V^2)
    """

    def __init__(self, directed=False):
        self.matrix = list()
        self.directed = directed

    def add_vertex(self):
        """
        Добавляет вершину в граф, расширяя матрицу смежности.
        """
        size = len(self.matrix)
        for row in self.matrix:
            row.append(0)
        self.matrix.append([0] * (size + 1))
    # Время: O(V)

    def remove_vertex(self, index):
        """
        Удаляет вершину из графа, сужая матрицу смежности.
        Args:
            index (int): Индекс вершины для удаления.
        """
        if index < 0 or index >= len(self.matrix):
            raise IndexError("Vertex index out of range")
        self.matrix.pop(index)
        for row in self.matrix:
            row.pop(index)
    # Время: O(V^2)

    def add_edge(self, u, v, weight=1):
        """
        Добавляет ребро между вершинами u и v с заданным весом.
        Args:
            u (int): Индекс начальной вершины.
            v (int): Индекс конечной вершины.
            weight (int): Вес ребра (по умолчанию 1).
        """
        if u < 0 or u >= len(self.matrix) or v < 0 or v >= len(self.matrix):
            raise IndexError("Vertex index out of range")
        self.matrix[u][v] = weight
        if not self.directed:
            self.matrix[v][u] = weight
    # Время: O(1)

    def remove_edge(self, u, v):
        """
        Удаляет ребро между вершинами u и v.
        Args:
            u (int): Индекс начальной вершины.
            v (int): Индекс конечной вершины.
        """
        if u < 0 or u >= len(self.matrix) or v < 0 or v >= len(self.matrix):
            raise IndexError("Vertex index out of range")
        self.matrix[u][v] = 0
        if not self.directed:
            self.matrix[v][u] = 0
    # Время: O(1)

    def list_to_matrix(self, adj_list):
        """
        Преобразует список смежности в матрицу смежности.
        Args:
            adj_list (AdjacencyList): Граф, представленный списком смежности.
        """
        size = len(adj_list.adj_list)
        self.matrix = [[0] * size for _ in range(size)]
        for u in adj_list.adj_list:
            for idx, v in enumerate(adj_list.adj_list[u]):
                weight = adj_list.weight_list[u][idx]
                self.matrix[u][v] = weight
    # Время: O(V^2)

    def print_matrix(self):
        """
        Печатает матрицу смежности графа.
        """
        for row in self.matrix:
            print(row)


class AdjacencyList:
    """
    Класс сущности списка смежности для представления графа.
    Attributes:
        adj_list (dict): Словарь, где ключи - вершины,
        а значения - списки смежных вершин.
        directed (bool): Флаг, указывающий, является ли граф ориентированным.
    Память: O(V + E)
    """

    def __init__(self, directed=False):
        self.adj_list = dict()
        self.weight_list = dict()
        self.directed = directed

    def add_vertex(self, vertex):
        """
        Добавляет вершину в граф.
        Args:
            vertex (int): Вершина для добавления.
        """
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            self.weight_list[vertex] = []
    # Время: O(1)

    def remove_vertex(self, vertex):
        """
        Удаляет вершину из графа.
        Args:
            vertex (int): Вершина для удаления.
        """
        if vertex in self.adj_list:
            self.adj_list.pop(vertex)
            self.weight_list.pop(vertex)
            for v in self.adj_list:
                if vertex in self.adj_list[v]:
                    self.adj_list[v].remove(vertex)
                    self.weight_list[v].pop(self.adj_list[v].index(vertex))
    # Время: O(V + E)

    def add_edge(self, u, v, weight=1):
        """
        Добавляет ребро между вершинами u и v с заданным весом.
        Args:
            u (int): Индекс начальной вершины.
            v (int): Индекс конечной вершины.
            weight (int): Вес ребра (по умолчанию 1).
        """
        if u not in self.adj_list:
            raise KeyError(f"Vertex {u} does not exist")
        if v not in self.adj_list:
            raise KeyError(f"Vertex {v} does not exist")
        self.adj_list[u].append(v)
        self.weight_list[u].append(weight)
        if not self.directed:
            self.adj_list[v].append(u)
            self.weight_list[v].append(weight)
    # Время: O(1)

    def remove_edge(self, u, v):
        """
        Удаляет ребро между вершинами u и v.
        Args:
            u (int): Индекс начальной вершины.
            v (int): Индекс конечной вершины.
        """
        if u in self.adj_list and v in self.adj_list[u]:
            self.adj_list[u].remove(v)
            self.weight_list[u].pop(self.adj_list[u].index(v))
            if not self.directed:
                self.adj_list[v].remove(u)
                self.weight_list[v].pop(self.adj_list[v].index(u))
    # Время: O(E)

    def matrix_to_list(self, adj_matrix):
        """
        Преобразует матрицу смежности в список смежности.
        Args:
            adj_matrix (AdjacencyМatrix): Граф, 
            представленный матрицей смежности.
        """
        size = len(adj_matrix.matrix)
        self.adj_list = {i: [] for i in range(size)}
        self.weight_list = {i: [] for i in range(size)}
        for u in range(size):
            for v in range(size):
                if adj_matrix.matrix[u][v] != 0:
                    self.adj_list[u].append(v)
                    self.weight_list[u].append(adj_matrix.matrix[u][v])
    # Время: O(V^2)

    def print_list(self):
        """
        Печатает список смежности графа.
        """
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")
