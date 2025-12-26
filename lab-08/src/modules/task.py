# task.py

import sys


def min_coins_greedy(coins, amount):
    """
    Находит минимальное количество монет для выдачи суммы amount
    с помощью жадного алгоритма.

    Args:
        coins (list): Доступные номиналы монет.
        amount (int): Сумма, которую нужно выдать.

    Returns:
        list: Список монет, составляющих сумму amount.
    """
    coins = sorted(coins, reverse=True)  # сортируем по убыванию
    result = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    return result


def prim_mst(graph):
    """
    Алгоритм построение минимального остовного дерева алгоритмом прима

    Args:
        graph: матрица смежности, graph[u][v] = вес ребра u-v, 0 если ребра нет

    Returns:
        список ребер MST и их суммарный вес
    """
    V = len(graph)
    selected = [False] * V  # вершины, включённые в MST
    key = [sys.maxsize] * V  # минимальные веса для подключения вершины к MST
    parent = [-1] * V  # родительские вершины в MST

    key[0] = 0  # начинаем с вершины 0

    for _ in range(V):
        # выбираем вершину с минимальным ключом, ещё не включённую в MST
        min_key = sys.maxsize
        u = -1
        for v in range(V):
            if not selected[v] and key[v] < min_key:
                min_key = key[v]
                u = v

        selected[u] = True  # включаем вершину в MST

        # обновляем ключи для смежных вершин
        for v in range(V):
            if graph[u][v] > 0 and not selected[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    # формируем MST
    mst_edges = []
    total_weight = 0
    for v in range(1, V):
        mst_edges.append((parent[v], v, graph[parent[v]][v]))
        total_weight += graph[parent[v]][v]

    return mst_edges, total_weight
