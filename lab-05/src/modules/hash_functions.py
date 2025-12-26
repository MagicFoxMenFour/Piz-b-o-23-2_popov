# hash_functions.py

def simple_hash(str):
    """
    Вычисляет хеш для строки.

    Args:
        str: Входная строка.
        len: длина массива.

    Returns:
        Значение хеша строки.
    """
    sum = 0
    for i in str:
        sum += ord(i)
    return sum
    # Временная сложность: O(n) — нужно пройти по всем символам строки


def polynomial_hash(str, p=37, mod=10**9 + 7):
    """
    Вычисляет полиномиальный хеш для строки.

    Args:
        str: Входная строка.
        p: Простое число (основание хеша).
        mod: Большое число (модуль хеширования).

    Returns:
        Значение хеша строки.
    """
    hash_value = 0
    p_pow = 1
    for i in str:
        char_code = ord(i)
        hash_value = (hash_value + char_code * p_pow) % mod
        p_pow = (p_pow * p) % mod
    return hash_value
    # Временная сложность: O(n) — один проход по символам


def djb2_hash(str):
    """
    Вычисляет DJB2 хеш для строки.

    Args:
        str: Входная строка.

    Returns:
        Значение хеша строки.
    """
    hash_value = 5381
    for i in str:
        hash_value = ((hash_value << 5) + hash_value) + \
            ord(i)  # hash * 33 = (2^5 + 1(hash)) + ord(i)
    return hash_value & 0xFFFFFFFF  # для ограничения 32-битного числа
    # Временная сложность: O(n) — один проход по символам
