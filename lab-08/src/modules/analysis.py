# analysis.py

from itertools import combinations
from modules.greedy_algorithms import fractional_knapsack


def greedy_discrete_knapsack(items, capacity):
    """Жадный алгоритм для дискретного рюкзака
    (0-1), без дробления предметов."""
    items = sorted(items, key=lambda x: x[0]/x[1], reverse=True)
    total_value = 0
    taken_items = []
    for value, weight in items:
        if weight <= capacity:
            total_value += value
            capacity -= weight
            taken_items.append((value, weight))
    return total_value, taken_items


def knapsack_bruteforce(items, capacity):
    """Точный перебор для дискретного (0-1) рюкзака."""
    n = len(items)
    best_value = 0
    best_combo = []
    for r in range(1, n + 1):
        for combo in combinations(items, r):
            total_weight = sum(w for _, w in combo)
            total_value = sum(v for v, _ in combo)
            if total_weight <= capacity and total_value > best_value:
                best_value = total_value
                best_combo = combo
    return best_value, best_combo


def analysis():
    """
    Анализ и сравнение жадных алгоритмов
    и точного перебора для задачи о рюкзаке.
    1. Жадный алгоритм для непрерывного рюкзака (fractional knapsack).
    2. Жадный алгоритм для дискретного рюкзака (0-1 knapsack).
    3. Точный перебор для дискретного рюкзака (0-1 knapsack).
    """
    # Пример данных
    items = [(60, 10), (100, 20), (120, 30)]  # (стоимость, вес)
    capacity = 50

    # Алгоритмы
    frac_value = fractional_knapsack(items, capacity)
    greedy_value, greedy_combo = greedy_discrete_knapsack(items, capacity)
    brute_value, brute_combo = knapsack_bruteforce(items, capacity)

    # Вывод
    print("Рюкзак емкостью:", capacity)
    print("Предметы (стоимость, вес):", items)
    print("Жадный алгоритм (непрерывный рюкзак):", frac_value)
    print("Жадный алгоритм (дискретный 0-1 рюкзак):", greedy_value,
          greedy_combo)
    print("Точный перебор (дискретный 0-1 рюкзак):", brute_value, brute_combo)
