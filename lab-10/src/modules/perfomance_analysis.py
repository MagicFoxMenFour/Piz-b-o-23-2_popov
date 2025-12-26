# perfomance_analysis.py

from modules.graph_representation import AdjacencyМatrix
from modules.graph_representation import AdjacencyList
import timeit
import matplotlib.pyplot as plt
# Сравнение add Vertex(matrix, list), Remove Vertex(matrix, list)


def measure_time_matrix(size):
    """
    Измеряет время добавления и удаления вершин
    в графе, представленном матрицей смежности.
    Args:
        size (int): Количество вершин для добавления и удаления.
    Returns:
        tuple: Время добавления и удаления вершин в миллисекундах."""
    matrix = AdjacencyМatrix()

    start = timeit.default_timer()
    for _ in range(size):
        matrix.add_vertex()
    end = timeit.default_timer()
    matrix_add = (end - start) * 1000

    start = timeit.default_timer()
    for _ in range(size):
        matrix.remove_vertex(0)
    end = timeit.default_timer()
    matrix_remove = (end - start) * 1000

    return (matrix_add, matrix_remove)


def measure_time_list(size):
    """
    Измеряет время добавления и удаления вершин
    в графе, представленном списком смежности.
    Args:
        size (int): Количество вершин для добавления и удаления.
    Returns:
        tuple: Время добавления и удаления вершин в миллисекундах.
    """
    lst = AdjacencyList()

    start = timeit.default_timer()
    for i in range(size):
        lst.add_vertex(i)
    end = timeit.default_timer()
    list_add = (end - start) * 1000

    start = timeit.default_timer()
    for _ in range(size):
        lst.remove_vertex(0)
    end = timeit.default_timer()
    list_remove = (end - start) * 1000

    return (list_add, list_remove)


def Visualisation(sizes):
    """
    Визуализирует результаты измерений
    времени добавления и удаления вершин
    для матрицы и списка смежности.
    Args:
        sizes (list): Список размеров графов для измерений.
    """

    matrix_add_times = []
    list_add_times = []
    matrix_remove_times = []
    list_remove_times = []

    for size in sizes:
        result = measure_time_matrix(size)
        matrix_add_times.append(result[0])
        matrix_remove_times.append(result[1])

        result = measure_time_list(size)
        list_add_times.append(result[0])
        list_remove_times.append(result[1])

    plt.plot(sizes, matrix_add_times, label='Matrix Add Vertex')
    plt.plot(sizes, list_add_times, label='List Add Vertex')
    plt.title('Add Vertex Performance')
    plt.xlabel('Number of Vertices')
    plt.ylabel('Time (ms)')
    plt.legend()
    plt.savefig('./report/add_vertex_performance.png')
    plt.show()

    plt.plot(sizes, matrix_remove_times, label='Matrix Remove Vertex')
    plt.plot(sizes, list_remove_times, label='List Remove Vertex')
    plt.title('Remove Vertex Performance')
    plt.xlabel('Number of Vertices')
    plt.ylabel('Time (ms)')
    plt.legend()
    plt.savefig('./report/remove_vertex_performance.png')
    plt.show()
