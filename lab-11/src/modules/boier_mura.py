# boier_mura.py

def boier_mura(pattern, text):
    """
    Выполняет поиск всех вхождений шаблона в текст
    с помощью алгоритма Бойера-Мура.
    Args:
        pattern (str): Шаблон для поиска.
        text (str): Текст, в котором выполняется поиск.
    Returns:
        list: Список начальных индексов всех вхождений шаблона в текст.
    """

    m = len(pattern)
    n = len(text)
    if m == 0 or n == 0 or m > n:
        return []

    # Создание таблицы смещений для символов
    bad_char = {}
    for i in range(m):
        bad_char[pattern[i]] = i

    occurrences = []
    s = 0  # сдвиг шаблона относительно текста
    while s <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            occurrences.append(s)
            s += (m - bad_char.get(text[s + m], -1)) if s + m < n else 1
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))

    return occurrences
# Время: O(n) в среднем случае
# Особенности: 
# Сравнение справа налево
# Использование таблицы плохих символов для оптимизации сдвигов
# Память: O(k), где k - размер алфавита
# Оптимален для больших алфавитов и длинных шаблонов
# В худшем случае O(n * m)
# Худший случай возникает при большом количестве
# совпадающих символов между шаблоном и текстом.
# Например, при поиске шаблона "aaaa" в тексте "aaaaaaaa".

