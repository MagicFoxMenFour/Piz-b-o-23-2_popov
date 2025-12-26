# recursion_tasks.py

import os


def binary_search_recursive(arr, target, left, right):
    """
    Рекурсивно ищет элемент target в отсортированном списке arr.
    Аргументы:
            arr: отсортированный список элементов.
            target: искомый элемент.
            left: левая граница поиска.
            right: правая граница поиска.
    Возвращает:
            Индекс target в arr, если найден, иначе -1.
    """
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, right)


def print_directory_tree(path, indent=""):
    """
    Рекурсивно выводит дерево каталогов и файлов, начиная с заданного пути.
    Аргументы:
        path: строка — путь к директории, с которой начинается обход.
        indent: строка — отступ для текущего уровня (служебный параметр).
    """
    print(f"{indent}{os.path.basename(path)}/")
    try:
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                print_directory_tree(full_path, indent + "    ")
            else:
                print(f"{indent}    {entry}")
    except PermissionError:
        print(f"{indent}    [Permission Denied]")


def hanoi(n, source, target, auxiliary):
    """
    Рекурсивно решает задачу Ханойские башни для n дисков и 3 стержней.
    Аргументы:
        n: количество дисков.
        source: имя исходного стержня (строка).
        target: имя целевого стержня (строка).
        auxiliary: имя вспомогательного стержня (строка).
    """
    if n == 1:
        print(f"Переместить диск 1 с {source} на {target}")
        return
    hanoi(n-1, source, auxiliary, target)
    print(f"Переместить диск {n} с {source} на {target}")
    hanoi(n-1, auxiliary, target, source)
