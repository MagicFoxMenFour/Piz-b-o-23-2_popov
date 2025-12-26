# string_matching.py

from modules.prefix_function import prefix_function
from modules.kmp_search import kmp_search


def find_period(string):
    """
    Находит минимальный период строки с помощью префикс-функции.
    Args:
        string (str): Входная строка.
    Returns:
        int: Длина минимального периода строки.
    """
    n = len(string)
    prefixs = prefix_function(string)
    period_length = n - prefixs[-1]
    if n % period_length == 0:
        return period_length
    else:
        return n


def cyclic_shift(a, b):
    """
    Проверяет, является ли строка b циклическим сдвигом строки a.
    Args:
        a (str): Первая строка.
        b (str): Вторая строка.
    Returns:
        bool: True, если b является циклическим сдвигом a, иначе False.
    """
    if kmp_search(a, b+b):
        return True
    return False

# def is_cyclic_shift(a, b):
#     """
#     Проверяет, является ли строка b циклическим сдвигом строки a.
#     Args:
#         a (str): Первая строка.
#         b (str): Вторая строка.
#     Returns:
#         bool: True, если b является циклическим сдвигом a, иначе False.
#     """
#     if len(a) != len(b):
#         return False
#     return b in (a + a)


# print(is_cyclic_shift("abcd", "cdab"))  # True
# print(is_cyclic_shift("abcd", "acbd"))  # False
