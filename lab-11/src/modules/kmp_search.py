# kmp_search.py

from modules.prefix_function import prefix_function
# from src.modules.prefix_function import prefix_function  # tests


def kmp_search(pattern, text):
    """
    Выполняет поиск всех вхождений шаблона в текст
    с помощью алгоритма Кнута-Морриса-Пратта (КМП).
    Args:
        pattern (str): Шаблон для поиска.
        text (str): Текст, в котором выполняется поиск.
    Returns:
        list: Список начальных индексов всех вхождений шаблона в текст.
    """
    prefixs = prefix_function(pattern)
    m = len(pattern)
    n = len(text)
    j = 0
    occurrences = []

    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = prefixs[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            occurrences.append(i - m + 1)
            j = prefixs[j - 1]

    return occurrences
# Время: O(n + m)
# Память: O(m)
# В худшем случае O(n * m)
# Худший случай возникает при большом количестве
# совпадающих префиксов между шаблоном и текстом.
# Например, при поиске шаблона "aaaa" в тексте "aaaaaaaa".


def naive_search(pattern, text):
    """
    Выполняет наивный поиск всех вхождений шаблона в текст.
    Args:
        pattern (str): Шаблон для поиска.
        text (str): Текст, в котором выполняется поиск.
    Returns:
        list: Список начальных индексов всех вхождений шаблона в текст.
    """
    m = len(pattern)
    n = len(text)
    occurrences = []

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            occurrences.append(i)

    return occurrences
# Время: O(n * m) в худшем случае
# Память: O(1)
