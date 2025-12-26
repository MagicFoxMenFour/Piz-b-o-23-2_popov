# perfomance_analysis.py

from modules.kmp_search import kmp_search, naive_search
from modules.z_function import find_substring_z
from modules.boier_mura import boier_mura
import timeit
from matplotlib import pyplot as plt

# График сравнения алгоритмов фиксированный паттерн, но увеличение текста
# График сравнения алгоритмов фиксированный текст, но увеличение паттерна


def generate_random_string(size):
    """
    Генерирует случайную строку заданного размера.
    Args:
        size: Размер строки.
    Returns:
        str: Случайная строка.
    """
    alphabet = 'abcde'
    import random
    return ''.join(random.choices(alphabet, k=size))


def measure_time_fix_pat(size, pat_size=25):
    """
    Измеряет время выполнения алгоритмов при фиксированном размере паттерна
    и изменяющемся размере текста.
    Args:
        size: Размер текста.
        pat_size: Размер паттерна.
    Returns:
        tuple: Времена выполнения для каждого алгоритма.
    """
    text = generate_random_string(size)
    pattern = generate_random_string(pat_size)

    kmp_time = timeit.timeit(lambda: kmp_search(pattern, text), number=10)
    naive_time = timeit.timeit(lambda: naive_search(pattern, text), number=10)
    z_time = timeit.timeit(lambda: find_substring_z(pattern, text), number=10)
    boier_mura_time = timeit.timeit(
        lambda: boier_mura(pattern, text), number=10)

    return (kmp_time * 1000, naive_time * 1000,
            z_time * 1000, boier_mura_time * 1000)


def measure_time_fix_text(pat_sizes, size=100000):
    """
    Измеряет время выполнения алгоритмов при фиксированном размере текста
    и изменяющемся размере паттерна.
    Args:
        pat_sizes: Размер паттерна.
        size: Размер текста.
    Returns:
        tuple: Времена выполнения для каждого алгоритма."""
    text = generate_random_string(size)
    pattern = generate_random_string(pat_sizes)

    kmp_time = timeit.timeit(lambda: kmp_search(pattern, text), number=10)
    naive_time = timeit.timeit(lambda: naive_search(pattern, text), number=10)
    z_time = timeit.timeit(lambda: find_substring_z(pattern, text), number=10)
    boier_mura_time = timeit.timeit(
        lambda: boier_mura(pattern, text), number=10)

    return (kmp_time * 1000, naive_time * 1000,
            z_time * 1000, boier_mura_time * 1000)


def Visualisation(Sizes, pat_sizes):
    """
    Визуализирует результаты измерений времени выполнения алгоритмов.
    Args:
        Sizes: Список размеров текста.
        pat_sizes: Список размеров паттерна.
    """
    kmp_times_fix_pat = []
    naive_times_fix_pat = []
    z_times_fix_pat = []
    boier_mura_times_fix_pat = []

    for size in Sizes:
        kmp_time, naive_time, z_time, boier_mura_time = measure_time_fix_pat(
            size)
        kmp_times_fix_pat.append(kmp_time)
        naive_times_fix_pat.append(naive_time)
        z_times_fix_pat.append(z_time)
        boier_mura_times_fix_pat.append(boier_mura_time)

    print("Measures for fixed pattern size:")
    print("Sizes:", Sizes)
    print("KMP times:", kmp_times_fix_pat)
    print("Naive times:", naive_times_fix_pat)
    print("Z-Function times:", z_times_fix_pat)
    print("Boier-Mura times:", boier_mura_times_fix_pat)

    plt.figure(figsize=(12, 6))
    plt.plot(Sizes, kmp_times_fix_pat, label='KMP Search')
    plt.plot(Sizes, naive_times_fix_pat, label='Naive Search')
    plt.plot(Sizes, z_times_fix_pat, label='Z-Function Search')
    plt.plot(Sizes, boier_mura_times_fix_pat, label='Boier-Mura Search')
    plt.xlabel('Size of Text')
    plt.ylabel('Time (mseconds)')
    plt.title('Performance Comparison (Fixed Pattern Size)')
    plt.legend()
    plt.grid()
    plt.savefig('./report/fix_pattern.png')
    plt.show()

    kmp_times_fix_text = []
    naive_times_fix_text = []
    z_times_fix_text = []
    boier_mura_times_fix_text = []

    for pat_size in pat_sizes:
        kmp_time, naive_time, z_time, boier_mura_time = measure_time_fix_text(
            pat_size)
        kmp_times_fix_text.append(kmp_time)
        naive_times_fix_text.append(naive_time)
        z_times_fix_text.append(z_time)
        boier_mura_times_fix_text.append(boier_mura_time)

    print("Measures for fixed text size:")
    print("Pattern Sizes:", pat_sizes)
    print("KMP times:", kmp_times_fix_text)
    print("Naive times:", naive_times_fix_text)
    print("Z-Function times:", z_times_fix_text)
    print("Boier-Mura times:", boier_mura_times_fix_text)

    plt.figure(figsize=(12, 6))
    plt.plot(pat_sizes, kmp_times_fix_text, label='KMP Search')
    plt.plot(pat_sizes, naive_times_fix_text, label='Naive Search')
    plt.plot(pat_sizes, z_times_fix_text, label='Z-Function Search')
    plt.plot(pat_sizes, boier_mura_times_fix_text, label='Boier-Mura Search')
    plt.xlabel('Size of Pattern')
    plt.ylabel('Time (mseconds)')
    plt.title('Performance Comparison (Fixed Text Size)')
    plt.legend()
    plt.grid()
    plt.savefig('./report/fix_text.png')
    plt.show()
