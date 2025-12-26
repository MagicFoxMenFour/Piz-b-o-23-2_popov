# generate_data.py

import random


def generate_random_data(size):
    """
    Генерирует список случайных целых чисел заданной длины.
    Аргументы:
        size: целое число - размер возвращаемого списка.
    Возвращает:
        Список целых чисел длины size,
        заполненный случайными значениями от 0 до 1_000_000.
    """
    ar = []
    for i in range(size):
        ar.append(random.randint(0, 1_000_000))
    return ar


def generate_sorted_data(size):
    """
    Генерирует отсортированный по возрастанию список случайных целых чисел.
    Аргументы:
        size: целое число - размер возвращаемого списка.
    Возвращает:
        Список целых чисел длины size, отсортированный по возрастанию.
    """
    ar = generate_random_data(size)
    ar.sort()
    return ar


def generate_reversed_data(size):
    """
    Генерирует список случайных целых чисел и выполняет его реверс.
    Аргументы:
        size: целое число - размер возвращаемого списка.
    Возвращает:
        Список целых чисел длины size, элементы которого расположены в
        обратном порядке (по сравнению с исходным случайным списком).
    """
    ar = generate_sorted_data(size)
    return list(reversed(ar))


def generate_almost_sorted_data(size):
    """
    Генерирует почти отсортированный список целых чисел.
    Аргументы:
        size: целое число - размер возвращаемого списка.
    Возвращает:
        Список целых чисел длины size, в котором примерно 5% элементов
        случайным образом перемешаны (остальные элементы отсортированы).
    """
    ar = generate_sorted_data(size)
    for i in range(size // 20):
        ind1 = random.randint(0, len(ar) - 1)
        ind2 = random.randint(0, len(ar) - 1)
        temp = ar[ind1]
        ar[ind1] = ar[ind2]
        ar[ind2] = temp
    return ar
