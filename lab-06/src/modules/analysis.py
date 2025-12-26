# analysis.py

import random
import time
from modules.binary_search_tree import BinarySearchTree


def build_random_tree(size):
    """
    Генерирует сбалансированное бинарное дерево

    Args:
        size: Количество узлов в дереве

    Returns:
        tree: Сбалансированное бинарное дерево поиска
    """
    values = list(range(size))
    random.shuffle(values)
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree


def build_sorted_tree(size):
    """
    Генерирует вырожденное бинарное дерево

    Args:
        size: Количество узлов в дереве

    Returns:
        tree: Вырожденное бинарное дерево поиска
    """
    values = list(range(size))
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree


def measure_search_time(tree, size, trials=1000):
    """
    Измеряет время выполнения 1000 операций поиска в бинарном
    дереве

    Args:
        tree: Бинарное дерево поиска
        size: Размер дерева
        trials: Количество операций поиска

    Returns:
        out: Время выполнения всех операций поиска в секундах
    """
    keys = [random.randrange(size) for _ in range(trials)]
    start = time.perf_counter()
    for k in keys:
        tree.search(k)
    end = time.perf_counter()
    return end - start


def run_experiment(sizes, trials_per_size=1000, repeats=5):
    """
    Измеряет среднее время выполнения операций поиска для сбалансированного
    и вырожденного бинарного дерева

    Args:
        sizes: Список размеров деревьев для тестирования
        trials_per_size: Количество операций поиска для каждого размера
        repeats: Количество повторений эксперимента для усреднения

    Returns:
        results: Список кортежей (размер, время_сбалансированного,
                время_вырожденного)
    """
    results = []
    for n in sizes:
        balanced_times = []
        degenerate_times = []
        for r in range(repeats):
            t_bal = build_random_tree(n)
            bt = measure_search_time(t_bal, n, trials=trials_per_size)
            balanced_times.append(bt)

            t_deg = build_sorted_tree(n)
            dt = measure_search_time(t_deg, n, trials=trials_per_size)
            degenerate_times.append(dt)

        balanced_avg = sum(balanced_times) / repeats
        degenerate_avg = sum(degenerate_times) / repeats
        results.append((n, balanced_avg, degenerate_avg))
        print(
            f"n={n}: Сбалансированное avg {balanced_avg:.6f}s, "
            f"Вырожденное avg {degenerate_avg:.6f}s"
        )

    return results
