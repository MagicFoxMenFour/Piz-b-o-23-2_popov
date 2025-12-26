# z-function.py

def z_function(string):
    """
    Вычисляет Z-функцию для заданной строки.
    Args:
        string (str): Входная строка.
    Returns:
        list: Список Z-функций для каждого префикса строки.
    """
    n = len(string)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and string[z[i]] == string[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z
# Время: O(n)
# Память: O(n)


def find_substring_z(pattern, text):
    """
    Выполняет поиск всех вхождений шаблона в текст
    с помощью Z-функции.
    Args:
        pattern (str): Шаблон для поиска.
        text (str): Текст, в котором выполняется поиск.
    Returns:
        list: Список начальных индексов всех вхождений шаблона в текст.
    """
    combined = pattern + "$" + text
    z = z_function(combined)
    m = len(pattern)
    occurrences = []

    for i in range(len(z)):
        if z[i] == m:
            occurrences.append(i - m - 1)

    return occurrences
# Время: O(n + m)
# Память: O(n + m)
# В худшем случае O(n * m)
# Худший случай возникает при большом количестве
# совпадающих префиксов между шаблоном и текстом.
# Например, при поиске шаблона "aaaa" в тексте "aaaaaaaa".
