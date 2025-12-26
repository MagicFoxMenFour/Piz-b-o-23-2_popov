# prefix_function.py

def prefix_function(string):
    """
    Вычисляет префикс-функцию для заданной строки.
    Args:
        string (str): Входная строка.
    Returns:
        list: Список префикс-функций для каждого префикса строки.
    """
    n = len(string)
    prefixs = [0] * n
    for i in range(1, n):
        j = prefixs[i - 1]
        while j > 0 and string[i] != string[j]:
            j = prefixs[j - 1]
        if string[i] == string[j]:
            j += 1
        prefixs[i] = j
    return prefixs
# Время: O(n)
# Память: O(n)