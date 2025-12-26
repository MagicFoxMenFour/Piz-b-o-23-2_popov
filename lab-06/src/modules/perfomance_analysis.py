# perfomance_analysis.py

import random
import timeit
import matplotlib.pyplot as plt

from modules.binary_search_tree import BinarySearchTree


def build_tree(n, balanced=True):
    """
    Создает бинарное дерево поиска заданного размера.

    Args:
        n: Количество узлов в дереве
        balanced: Флаг создания сбалансированного дерева

    Returns:
        tree: Созданное бинарное дерево поиска
    """
    values = list(range(n))
    if balanced:
        random.shuffle(values)
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree


def time_insert(n, balanced=True):
    """
    Измеряет время выполнения для операции вставки в бинарное дерево

    Args:
        n: Размер дерева
        balanced: Флаг использования сбалансированного дерева

    Returns:
        out: Время выполнения вставки в миллисекундах
    """
    tree = build_tree(n, balanced=balanced)

    new_value = n
    start = timeit.default_timer()
    tree.insert(new_value)
    end = timeit.default_timer()
    return (end - start) * 1000


def measure_time(sizes):
    """
    Вычисляет среднее время выполнения для сбалансированного и
    вырожденного бинарного дерева.

    Args:
        sizes: Список размеров деревьев для тестирования

    Returns:
        res: Словарь с результатами измерений для разных размеров деревьев
    """
    res = {'sizes': list(sizes), 'balanced': [], 'degenerate': []}

    for n in sizes:
        res['balanced'].append(time_insert(n, True))
        res['degenerate'].append(time_insert(n, False))

    return res


def visualisation(sizes, out_png=None):
    """
    Визуализирует график зависимости времени выполнения
    от размера бинарного дерева

    Args:
        sizes: Список размеров деревьев для визуализации
        out_png: Путь к файлу для сохранения графика
    """
    series = measure_time(sizes)
    x = series['sizes']
    plt.plot(x, series['balanced'], marker='o', label='Сбалансированное '
             '(insert)')
    plt.plot(x, series['degenerate'], marker='o', label='Вырожденное (insert)')
    plt.xlabel('n')
    plt.ylabel('time(ms)')
    plt.title('BST insert time: Сбалансированное vs Вырожденное')
    plt.legend()
    if out_png:
        plt.savefig(out_png, dpi=300, bbox_inches='tight')
    plt.show()
