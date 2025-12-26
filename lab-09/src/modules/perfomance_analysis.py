# perfomance_analysis.py

import tracemalloc
import timeit
import random
from modules.dynamic_programming import (
    knapsack_01, fib_tabulation, lcs, levenshtein_distance)
import matplotlib.pyplot as plt


# --- knapsack ---

def measure_performance(func, weights, values, capacity):
    """
    Измеряет время и память для функции func
    при заданных весах, значениях и емкости рюкзака.
    Args:
        func: функция для измерения
        weights: список весов предметов
        values: список стоимостей предметов
        capacity: максимальная емкость рюкзака
    Returns:
        tuple: (время выполнения в мс, потребляемая память в КБ)
    """
    time = []
    memory = []

    tracemalloc.start()
    start_time = timeit.default_timer()

    func(weights, values, capacity)

    end_time = timeit.default_timer()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    time = ((end_time - start_time) * 1000)
    memory = (peak / 1024)  # в КБ

    return time, memory


def generate_items(capacitiy):
    """
    Генерирует случайные веса и стоимости предметов
    для задачи рюкзака.
    Args:
        capacitiy: максимальная емкость рюкзака
    Returns:
        tuple: (список весов, список стоимостей)
    """
    weights = []
    values = []
    for i in range(capacitiy * 10):
        weights.append(random.randint(0, capacitiy // 10))
        values.append(random.randint(0, capacitiy * 10))
    return weights, values


def visualization_knapsack(capacities):
    """
    Визуализация анализа производительности
    алгоритма рюкзака 0/1
    Args:
        capacities: список емкостей рюкзака для анализа
    """
    knap_time = []
    knap_mem = []
    for i in capacities:
        weights, values = generate_items(i)
        knap_time_i, knap_mem_i = measure_performance(
            knapsack_01, weights, values, i)
        knap_time.append(knap_time_i)
        knap_mem.append(knap_mem_i)

    plt.subplot(1, 2, 1)
    plt.plot(capacities, knap_time, label='Knapsack 0/1', marker='o')
    plt.title('Время выполнения Knapsack 0/1 vs Capacity')
    plt.xlabel('Capacity')
    plt.ylabel('Время (ms)')
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(capacities, knap_mem, label='Knapsack 0/1', marker='o')
    plt.title('Потребление памяти Knapsack 0/1 vs Capacity')
    plt.xlabel('Capacity')
    plt.ylabel('Память (КБ)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig('./report/knapsack_analysis.png')
    plt.show()

# --- fib ---


def visualization_fib(n_values):
    """
    Визуализация анализа производительности
    алгоритма вычисления чисел Фибоначчи с табуляцией.
    Args:
        n_values: список значений n для анализа
    """
    time = []
    for n in n_values:
        start_time = timeit.default_timer()
        fib_tabulation(n)
        end_time = timeit.default_timer()
        time.append((end_time - start_time) * 1000)

    plt.plot(n_values, time, label='Fib Tabulation', marker='o')
    plt.title('Время выполнения Fibonacci Tabulation vs n')
    plt.xlabel('n')
    plt.ylabel('Время (ms)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('./report/fib_tabulation_analysis.png')
    plt.show()

# --- lcs ---


def generate_strings(length):
    """
    Генерирует две случайные строки заданной длины.
    Args:
        length: длина строк
    Returns:
        tuple: (строка 1, строка 2)
    """
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    str1 = ''.join(random.choice(letters) for _ in range(length))
    str2 = ''.join(random.choice(letters) for _ in range(length))
    return str1, str2


def visualization_lcs(lengths):
    """
    Визуализация анализа производительности
    алгоритма нахождения наибольшей общей подпоследовательности (LCS).
    Args:
        lengths: список длин строк для анализа
    """
    lcs_time = []
    for length in lengths:
        str1, str2 = generate_strings(length)
        start_time = timeit.default_timer()
        lcs(str1, str2)
        end_time = timeit.default_timer()
        lcs_time.append((end_time - start_time) * 1000)

    plt.plot(lengths, lcs_time, label='LCS', marker='o')
    plt.title('Время выполнения LCS vs Length')
    plt.xlabel('Length')
    plt.ylabel('Время (ms)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('./report/lcs_analysis.png')
    plt.show()

# --- levenshtein ---


def visualization_levenshtein(lengths):
    """
    Визуализация анализа производительности
    алгоритма вычисления расстояния Левенштейна.
    Args:
        lengths: список длин строк для анализа
    """
    lev_time = []
    for length in lengths:
        str1, str2 = generate_strings(length)
        start_time = timeit.default_timer()
        levenshtein_distance(str1, str2)
        end_time = timeit.default_timer()
        lev_time.append((end_time - start_time) * 1000)

    plt.plot(lengths, lev_time, label='Levenshtein Distance', marker='o')
    plt.title('Время выполнения Levenshtein Distance vs Length')
    plt.xlabel('Length')
    plt.ylabel('Время (ms)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('./report/levenshtein_analysis.png')
    plt.show()
