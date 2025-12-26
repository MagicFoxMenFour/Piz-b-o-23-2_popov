# main.py

import sys
from modules.comparison import visualization
from modules.comparison import analysis
from modules.dynamic_programming import (
    lcs_with_sequence, fib_tabulation_with_print)
from modules.tasks import coin_change, lis
from modules.perfomance_analysis import (
    visualization_knapsack, visualization_fib, visualization_lcs,
    visualization_levenshtein)


sys.setrecursionlimit(30000)  # увеличиваем лимит рекурсии для больших n
# можно увеличить до 2000-5000 для наглядности
n_values = list(range(100, 1001, 100))
visualization(n_values)

print("\n")

analysis()

print("\n")


# Пример использования:
length, subseq = lcs_with_sequence("AGGTAB", "GXTXAYB")
print(length)
print(subseq)

print("\n")

# --- Пример использования ---
coins = [1, 2, 5]
amount = 11

min_coins = coin_change(coins, amount)
print(f"Минимальное количество монет для {amount}:", min_coins)

print("\n")

# --- Пример использования ---
seq = [10, 22, 9, 33, 21, 50, 41, 60]
length, subsequence = lis(seq)
print("Длина LIS:", length)            # 5
print("LIS:", subsequence)            # [10, 22, 33, 50, 60]

print("\n")

n_values = [100, 1000, 5000, 10000, 25000]
visualization_fib(n_values)

capasities = list(range(100, 501, 100))
visualization_knapsack(capasities)

lengths = [10, 50, 100, 250, 500, 1000, 2500, 10000]
visualization_lcs(lengths)
visualization_levenshtein(lengths)

fib_tabulation_with_print(10)

# Характеристики вычислительной машины
pc_info = """
Характеристики ПК для тестирования:
- Процессор: Intel Core i5-11500H @ 2.50GHz
- Оперативная память: 8 GB DDR4
- ОС: Windows 11
- Python: 3.12
"""
print(pc_info)
