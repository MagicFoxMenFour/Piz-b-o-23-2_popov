# main.py

from modules.greedy_algorithms import interval_scheduling, generate_intervals
from modules.greedy_algorithms import fractional_knapsack, generate_items
from modules.greedy_algorithms import (huffman_coding, generate_frequencies,
                                       generate_text, build_tree, print_tree)
from modules.analysis import analysis
from modules.task import min_coins_greedy, prim_mst
from modules.perfomance_analysis import visualization

# Пример использования:
intervals = generate_intervals(50)
result = interval_scheduling(intervals)
print("Выбранные интервалы:", result)

print("\n")

# Пример использования:
items = generate_items(10)
capacity = 50

result = fractional_knapsack(items, capacity)
print(f"Максимальная стоимость: {result:.2f}")

print("\n")

# Пример использования:
frequencies = generate_frequencies(generate_text(50))

codes = huffman_coding(frequencies)
print("Коды Хаффмана:")
for char, code in codes.items():
    print(f"{char}: {code}")

tree = build_tree(codes)
print_tree(tree)

print("\n")

# Запуск анализа и сравнения алгоритмов рюкзака
analysis()

print("\n")

# Пример: стандартная система монет (рубли)
coins = [1, 2, 5, 10]
amount = 28

result = min_coins_greedy(coins, amount)
print("Сдача:", result)
print("Количество монет:", len(result))

print("\n")

# Пример графа (матрица смежности)
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

mst_edges, total_weight = prim_mst(graph)
print("Ребра MST:")
for u, v, w in mst_edges:
    print(f"{u} - {v} (вес {w})")
print("Суммарный вес MST:", total_weight)

print("\n")

# Визуализация времени выполнения алгоритма Хаффмана
sizes = [1000, 5000, 10_000, 50_000, 100_000, 500_000, 1_000_000]
visualization(sizes)

# Характеристики вычислительной машины
pc_info = """
Характеристики ПК для тестирования:
- Процессор: Intel Core i5-12500H @ 2.50GHz
- Оперативная память: 32 GB DDR4
- ОС: Windows 11
- Python: 3.12
"""
print(pc_info)
