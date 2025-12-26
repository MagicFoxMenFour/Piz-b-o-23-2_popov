# perfomance.analysis.py

from modules.heap import Heap
from modules.heapsort import heapsort
from modules.sorts import merge_sort, quick_sort
import matplotlib.pyplot as plt
import timeit
import random

# Последовательный insert в heap VS build_heap [1000, 5000, 10000, 25000]


def get_random_array(size):
    """
    Создаёт массив случайных чисел.

    Args:
        size: длина массива.

    Returns:
        array: Массив случайных чисел длинной size.
    """
    array = []
    for i in range(size):
        array.append(random.randint(0, 1_000_000))
    return array


def measure_linear_insert(size):
    """
    Измеряет время выполнения size операций
    вставки в кучу.

    Args:
        size: количество операций вставки -> кол-во 
        элементов кучи.

    Returns:
        result: время выполнение операций.
    """
    array = get_random_array(size)
    heap = Heap(True)
    start = timeit.default_timer()
    for i in array:
        heap.insert(i)
    end = timeit.default_timer()
    return (end - start) * 1000


def measure_build_heap(size):
    """
    Измеряет время выполнения операции построения
    кучи из массива

    Args:
        size: длина массива, необходима для генерации массива

    Returns:
        result: время выполнение операции.
    """
    array = get_random_array(size)
    heap = Heap(True)
    start = timeit.default_timer()
    heap.build_heap(array)
    end = timeit.default_timer()
    return (end - start) * 1000


def visualization_build(sizes):
    """
    Визуализирует результат сравнения операций вставки и операции
    построения кучи из массива в виде графика.
    Args:
        sizes: список длин массивов для тестирования.

    Возвращает:
        None. Сохраняет график
    """
    linear_insert = []
    build_heap = []
    for size in sizes:
        linear_insert.append(measure_linear_insert(size))
        build_heap.append(measure_build_heap(size))
    print("Построение кучи:")
    print(linear_insert)
    print(build_heap)
    print("")
    plt.plot(sizes, linear_insert, marker='o', color="red", label='insert')
    plt.plot(sizes, build_heap, marker='o', color="blue", label='build')
    plt.xlabel("Количество элементов n")
    plt.ylabel("Время выполнения ms")
    plt.title("Сравнение послед. insert и build_heap")
    plt.legend(loc="upper left", title="Методы")
    plt.savefig("./report/creating_heap.png", dpi=300, bbox_inches="tight")
    plt.show()

# Heapsort VS quick_sort VS merge_sort [1000, 5000, 10000, 25000, 100000]


def measure_heapsort(size):
    """
    Измеряет время выполнения сортировки heapsort для массива случайных чисел.

    Args:
        size: длина массива, используемая для генерации случайных чисел.

    Returns:
        result: время выполнения сортировки в миллисекундах.
    """
    array = get_random_array(size)
    start = timeit.default_timer()
    array = heapsort(array)
    end = timeit.default_timer()

    return (end - start) * 1000


def measure_quick_sort(size):
    """
    Измеряет время выполнения сортировки quick_sort для массива случайных чисел.

    Args:
        size: длина массива, используемая для генерации случайных чисел.

    Returns:
        result: время выполнения сортировки в миллисекундах.
    """
    array = get_random_array(size)
    start = timeit.default_timer()
    array = quick_sort(array)
    end = timeit.default_timer()
    return (end - start) * 1000


def measure_merge_sort(size):
    """
    Измеряет время выполнения сортировки merge_sort для массива случайных чисел.

    Args:
        size: длина массива, используемая для генерации случайных чисел.

    Returns:
        result: время выполнения сортировки в миллисекундах.
    """
    array = get_random_array(size)
    start = timeit.default_timer()
    array = merge_sort(array)
    end = timeit.default_timer()
    return (end - start) * 1000


def visualization_sort(sizes):
    """
    Визуализирует результаты сравнения сортировок:
    heapsort, quick_sort и merge_sort для разных размеров массивов.

    Args:
        sizes: список длин массивов для тестирования.

    Returns:
        None. Сохраняет график в ./report/sorting.png и отображает его.
    """
    heapsort_measures = []
    quick_sort_measures = []
    merge_sort_measures = []
    for size in sizes:
        heapsort_measures.append(measure_heapsort(size))
        quick_sort_measures.append(measure_quick_sort(size))
        merge_sort_measures.append(measure_merge_sort(size))

    print("Сравнение сортировок")
    print(heapsort_measures)
    print(quick_sort_measures)
    print(merge_sort_measures)
    print("")
    plt.plot(sizes, heapsort_measures, marker='o', color="red", label='heap')
    plt.plot(sizes, quick_sort_measures, marker='o',
             color="blue", label='quick')
    plt.plot(sizes, merge_sort_measures, marker='o',
             color="green", label='merge')
    plt.xlabel("Количество элементов n")
    plt.ylabel("Время выполнения ms")
    plt.title("Сравнение сортировок")
    plt.legend(loc="upper left", title="Методы")
    plt.savefig("./report/sorting.png", dpi=300, bbox_inches="tight")
    plt.show()

# Insert VS PEEK VS EXTRACT [1000, 5000, 10000, 25000, 100000]


def measure_insert(size):
    """
    Измеряет среднее время выполнения операции insert в куче.

    Args:
        size: количество элементов, вставляемых перед измерением.

    Returns:
        result: среднее время одной операции insert (в секундах).
    """
    repeats = 20
    heap = Heap(True)
    for i in range(size):
        heap.insert(random.randint(0, 1_000_000))
    start = timeit.default_timer()
    for i in range(repeats):
        heap.insert(random.randint(0, 1_000_000))
    end = timeit.default_timer()
    return (end - start) / 20


def measure_peek(size):
    """
    Измеряет среднее время выполнения операции peek в куче.

    Args:
        size: количество элементов, вставляемых перед измерением.

    Returns:
        result: среднее время одной операции peek (в секундах).
    """
    repeats = 20
    heap = Heap(True)
    for i in range(size):
        heap.insert(random.randint(0, 1_000_000))
    start = timeit.default_timer()
    for i in range(repeats):
        heap.peek()
    end = timeit.default_timer()
    return (end - start) / 20


def measure_extract(size):
    """
    Измеряет среднее время выполнения операции extract в куче.

    Args:
        size: количество элементов, вставляемых перед измерением.

    Returns:
        result: среднее время одной операции extract (в секундах).
    """
    repeats = 20
    heap = Heap(True)
    for i in range(size):
        heap.insert(random.randint(0, 1_000_000))
    start = timeit.default_timer()
    for i in range(repeats):
        heap.extract()
    end = timeit.default_timer()
    return (end - start) / 20


def visualization_operations(sizes):
    """
    Визуализирует результаты сравнения трёх операций кучи:
    insert, peek и extract.

    Args:
        sizes: список размеров кучи для тестирования.

    Returns:
        None. Сохраняет график
    """
    insert_measures = []
    peek_measures = []
    extract_measures = []
    for size in sizes:
        insert_measures.append(measure_insert(size))
        peek_measures.append(measure_peek(size))
        extract_measures.append(measure_extract(size))

    print("Сравнение операций")
    print(insert_measures)
    print(peek_measures)
    print(extract_measures)
    print("")
    plt.plot(sizes, insert_measures, marker='o', color="red", label='insert')
    plt.plot(sizes, peek_measures, marker='o', color="blue", label='peek')
    plt.plot(sizes, extract_measures, marker='o',
             color="green", label='extract')
    plt.xlabel("Количество элементов n")
    plt.ylabel("Время выполнения ns")
    plt.title("Сравнение операций кучи")
    plt.legend(loc="upper left", title="Методы")
    plt.savefig("./report/heap_operations.png", dpi=300, bbox_inches="tight")
    plt.show()
