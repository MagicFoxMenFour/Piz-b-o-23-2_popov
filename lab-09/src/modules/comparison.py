# comparison.py

import timeit
import tracemalloc
import matplotlib.pyplot as plt
from modules.dynamic_programming import fib_memo, fib_tabulation
from modules.dynamic_programming import knapsack_01_with_items


def measure_performance(func, n_values):
    """
    Измеряет время и память для функции func
    при различных значениях n.
    Args:
        func: функция для измерения
        n_values: список значений n для измерения
    Returns:
        tuple: (список времен, список потребляемой памяти)
    """
    times = []
    memories = []

    for n in n_values:
        tracemalloc.start()
        start_time = timeit.default_timer()
        func(n)

        end_time = timeit.default_timer()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        times.append((end_time - start_time) * 1000)
        memories.append(peak / 1024)  # в КБ

    return times, memories


def visualization(sizes):
    """
    Визуализация сравнения
    временной и пространственной сложности
    алгоритмов вычисления чисел Фибоначчи:
    1. С мемоизацией (top-down).
    2. С табуляцией (bottom-up).
    Args:
        sizes: список значений n для анализа
    """

    memo_times, memo_mem = measure_performance(fib_memo, sizes)
    bottom_times, bottom_mem = measure_performance(fib_tabulation, sizes)

    # --- Построение графиков ---

    print("Время выполнения (Top-Down):", memo_times)
    print("Время выполнения (Bottom-Up):", bottom_times)
    plt.figure(figsize=(12, 5))

    # Время
    plt.subplot(1, 2, 1)
    plt.plot(sizes, memo_times, label='Top-Down (Memoization)', marker='o')
    plt.plot(sizes, bottom_times, label='Bottom-Up (Tabulation)', marker='o')
    plt.title('Время выполнения vs n')
    plt.xlabel('n')
    plt.ylabel('Время (ms)')
    plt.legend()
    plt.grid(True)

    print("Память(Top-Down): ", memo_mem)
    print("Память(Bottom-Up): ", bottom_mem)

    # Память
    plt.subplot(1, 2, 2)
    plt.plot(sizes, memo_mem, label='Top-Down (Memoization)', marker='o')
    plt.plot(sizes, bottom_mem, label='Bottom-Up (Tabulation)', marker='o')
    plt.title('Потребление памяти vs n')
    plt.xlabel('n')
    plt.ylabel('Память (КБ)')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig('./report/fib_analysis.png')
    plt.show()


def greedy_discrete_knapsack(items, capacity):
    """
    Жадный алгоритм для дискретного рюкзака
    (0-1), без дробления предметов.

    Args:
        items: список кортежей (стоимость, вес) предметов
        capacity: максимальная емкость рюкзака
    Returns:
        tuple: (общая стоимость, список взятых предметов)
    """
    items = sorted(items, key=lambda x: x[0]/x[1], reverse=True)
    total_value = 0
    taken_items = []
    for value, weight in items:
        if weight <= capacity:
            total_value += value
            capacity -= weight
            taken_items.append((value, weight))
    return total_value, taken_items


def analysis():
    """
    Анализ и сравнение жадных алгоритмов
    и динамического программирования для задачи о рюкзаке.
    1. Жадный алгоритм для дискретного рюкзака (0-1 knapsack).
    2. ДП для дискретного рюкзака (0-1 knapsack).
    """
    # Пример данных
    items = [(60, 10), (100, 20), (120, 30)]  # (стоимость, вес)
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50

    # Алгоритмы
    greedy_value, greedy_combo = greedy_discrete_knapsack(items, capacity)
    dp_value, dp_combo = knapsack_01_with_items(weights, values, capacity)

    # Вывод
    print("Рюкзак емкостью:", capacity)
    print("Предметы (стоимость, вес):", items)
    print("Жадный алгоритм (дискретный 0-1 рюкзак):", greedy_value,
          greedy_combo)
    print("ДП (дискретный 0-1 рюкзак):", dp_value, dp_combo)
