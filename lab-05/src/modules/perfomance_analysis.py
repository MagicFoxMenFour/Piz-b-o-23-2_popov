# perfomance_analysis.py

from modules.hash_table_chaining import ChainingHashTable
from modules.hash_table_open_addressing import LinearHashTable
from modules.hash_table_open_addressing import DoubleHashingHashTable
import random
import string
import timeit
import matplotlib.pyplot as plt


def generate_random_string_loop(length):
    """
    Генерирует рандомную строку длины length

    Args:
        length: длина строки для генерации

    Returns:
        random_string: Сгенерированная строка
    """
    characters = string.ascii_letters + string.digits
    random_string = ""
    for _ in range(length):
        random_string += random.choice(characters)
    return random_string


def get_time_for_chained(load, size, strings):
    """
    Вычисляет среднее время вставкии в хеш таблицу
    реализованную методом цепочек

    Args:
        load: целевой коэффициент заполнения.
        size: количество элементов для вставки.
        strings: список ключей (строк) длины >= size для вставки.

    Returns:
        out: среднее время вставки всех элементов в миллисекундах,
               усреднённое по нескольким прогонам.
    """
    measures = []
    for j in range(20):
        table = ChainingHashTable(initial_size=size, load=load)
        start = timeit.default_timer()
        for i in range(size):
            table.insert(strings[i], i)
        end = timeit.default_timer()
        measures.append((end - start) * 1000)
    return sum(measures) / len(measures)


def get_time_for_linear(load, size, strings):
    """
    Вычисляет среднее время вставкии в хеш таблицу
    открытой адресации линейной пробации

    Args:
        load: целевой коэффициент заполнения.
        size: количество элементов для вставки.
        strings: список ключей (строк) длины >= size для вставки.

    Returns:
        out: среднее время вставки всех элементов в миллисекундах,
               усреднённое по нескольким прогонам.
    """
    measures = []
    for j in range(20):
        table = LinearHashTable(size=size, load=load)
        start = timeit.default_timer()
        for i in range(size):
            table.insert(strings[i], i)
        end = timeit.default_timer()
        measures.append((end - start) * 1000)
    return sum(measures) / len(measures)


def get_time_for_double(load, size, strings):
    """
    Вычисляет среднее время вставкии в хеш таблицу
    открытой адресации двойного хеширования

    Args:
        load: целевой коэффициент заполнения.
        size: количество элементов для вставки.
        strings: список ключей (строк) длины >= size для вставки.

    Returns:
        out: среднее время вставки всех элементов в миллисекундах,
               усреднённое по нескольким прогонам.
    """
    measures = []
    for j in range(20):
        table = DoubleHashingHashTable(size=size, load=load)
        start = timeit.default_timer()
        for i in range(size):
            table.insert(strings[i], i)
        end = timeit.default_timer()
        measures.append((end - start) * 1000)
    return sum(measures) / len(measures)


def measure_time(loades=[0.1, 0.5, 0.7, 0.9], size=1000):
    """
    Собирает результаты времени выполнения в словарь вида
    ["метод реализации"] - [список значений времени выполнения]

    Args:
        loades: список коэффициентов заполнения для тестирования.
        size: количество элементов, вставляемых в
            каждую таблицу при каждом замере.

    Returns:
        dict: словарь с ключами 'chain', 'linear', 'double' и значениями -
              списками средних времени (в миллисекундах)
              для каждого коэффициента заполнения.
    """
    strings = []
    chained_list = []
    linear_list = []
    double_list = []
    for i in range(size):
        strings.append(generate_random_string_loop(10))
    for i in loades:
        chained_list.append(get_time_for_chained(i, size, strings))
        linear_list.append(get_time_for_linear(i, size, strings))
        double_list.append(get_time_for_double(i, size, strings))

    result = {}
    result["chain"] = chained_list
    result["linear"] = linear_list
    result["double"] = double_list

    return result


def visualisation(loads=[0.1, 0.5, 0.7, 0.9], size=1000):
    """
    Визуализирует графики зависимости времени выполнения от
    коэффициента заполнения

    Args:
        loads: список коэффициентов заполнения для оси X.
        size: количество элементов, вставляемых в каждой таблице для измерения.
    """
    measures = measure_time(loades=loads, size=size)
    chained_list = measures["chain"]
    linear_list = measures["linear"]
    double_list = measures["double"]

    create_plot(chained_list, loads,
                "графики зависимости времени от коэффициента заполнения",
                "./report/chained_hashtable.png", label="chain")
    create_plot(linear_list, loads,
                "графики зависимости времени от коэффициента заполнения",
                "./report/linear_hashtable.png", label="linear")
    create_plot(double_list, loads,
                "графики зависимости времени от коэффициента заполнения",
                "./report/double_hashtable.png", label="double")


def create_plot(data, sizes, title, path, label):
    """
    Строит и сохраняет график времени работы сортировок для одного типа данных.
    Args:
        data: список значений времени (ms) для каждой точки по оси X.
        sizes: список коэффициентов заполнения (ось X).
        title: заголовок графика.
        path: путь для сохранения PNG-файла.
        label: подпись кривой на графике.
    """
    plt.plot(sizes, data,
             marker="o", color="red", label=label)

    plt.xlabel("коэффициент заполнения")
    plt.ylabel("Время выполнения ms")
    plt.title(title)
    plt.legend(loc="upper left", title="Метод")
    plt.savefig(path, dpi=300, bbox_inches="tight")
    plt.show()
