# greedy_algorithms.py

import heapq


def generate_intervals(n, start_range=0, end_range=1000):
    """
    Генерирует список случайных интервалов.

    Args:
        n: количество интервалов
        start_range: минимальное значение начала интервала
        end_range: максимальное значение конца интервала

    Returns:
        intervals: список кортежей (start, end)
    """
    import random

    intervals = []
    for _ in range(n):
        start = random.randint(start_range, end_range - 1)
        end = random.randint(start + 1, end_range)
        intervals.append((start, end))

    return intervals


def interval_scheduling(intervals):
    """
    Возвращает максимальное количество непересекающихся интервалов.

    Args:
        intervals: список кортежей (start, end)

    Returns:
        selected: список непересекающихся интервалов
    """
    # Сортируем интервалы по времени окончания
    intervals.sort(key=lambda x: x[1])

    selected = []
    last_end = float('-inf')

    for start, end in intervals:
        if start >= last_end:
            selected.append((start, end))
            last_end = end

    return selected
    # Временная сложность: O(n log n) из-за сортировки


def generate_items(n, value_range=(10, 100), weight_range=(1, 50)):
    """
    Генерирует список случайных предметов.

    Args:
        n: количество предметов
        value_range: кортеж (min_value, max_value)
        weight_range: кортеж (min_weight, max_weight)

    Returns:
        items: список кортежей (value, weight)
    """
    import random

    items = []
    for _ in range(n):
        value = random.randint(*value_range)
        weight = random.randint(*weight_range)
        items.append((value, weight))

    return items


def fractional_knapsack(items, capacity):
    """
    Возвращает максимальную суммарную стоимость для данного объема рюкзака.

    Args:
        items: список кортежей (value, weight)
        capacity: максимальный вес рюкзака

    Returns:
        total_value: максимальная суммарная стоимость
    """
    # Сортируем предметы по убыванию удельной стоимости (value / weight)
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0.0  # суммарная стоимость
    for value, weight in items:
        if capacity == 0:
            break

        if weight <= capacity:
            # Берем весь предмет
            total_value += value
            capacity -= weight
        else:
            # Берем часть предмета
            fraction = capacity / weight
            total_value += value * fraction
            capacity = 0  # рюкзак заполнен

    return total_value
    # Временная сложность: O(n log n) из-за сортировки


def generate_text(length):
    """
    Генерирует случайный текст заданной длины.

    Args:
        length: длина текста

    Returns:
        text: сгенерированная строка
    """
    import random
    import string

    characters = string.ascii_uppercase  # заглавные буквы A-Z
    text = ''.join(random.choice(characters) for _ in range(length))
    return text


def generate_frequencies(text):
    """
    Генерирует частоты символов в тексте.

    Args:
        text: входная строка

    Returns:
        frequencies: словарь {символ: частота}
    """
    frequencies = {}
    for char in text:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    return frequencies


class Node:
    def __init__(self, char, freq):
        self.char = char      # символ
        self.freq = freq      # частота
        self.left = None
        self.right = None

    # для корректной работы heapq
    def __lt__(self, other):
        return self.freq < other.freq


def huffman_coding(frequencies):
    """
    Строит коды Хаффмана для заданных частот символов.

    Args:
        frequencies: словарь {символ: частота}
    Returns:
        codes: словарь {символ: код}
    """
    # создаем очередь с приоритетом (минимальная куча)
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    # пока в куче больше одного элемента — объединяем два наименьших
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    # в конце в куче останется одно дерево
    root = heap[0]
    codes = {}

    def generate_codes(node, current_code):
        if node is None:
            return
        if node.char is not None:
            codes[node.char] = current_code
            return
        generate_codes(node.left, current_code + "0")
        generate_codes(node.right, current_code + "1")

    generate_codes(root, "")

    return codes
    # Временная сложность: O(n log n) из-за операций с кучей


def build_tree(codes):
    tree = {}
    for char, code in codes.items():
        node = tree
        for bit in code:
            if bit not in node:
                node[bit] = {}
            node = node[bit]
        node['char'] = char
    return tree


def print_tree(node, prefix=''):
    for key, child in node.items():
        if key == 'char':
            print(f"{prefix}: {child}")
        else:
            print(f"{prefix}{key}")
            print_tree(child, prefix + '  ')
