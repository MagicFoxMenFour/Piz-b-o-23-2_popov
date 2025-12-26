# sorts.py

def bubble_sort(ar):
    """
    Сортировка пузырьком.
    Сравнивает соседние элементы и меняет их местами,
    если они идут в неправильном порядке.
    Сложность: худший O(n^2), средний O(n^2), лучший O(n). Память: O(1).
    """

    for i in range(len(ar) - 1, 0, -1):
        for j in range(0, i):
            if (ar[j] > ar[j+1]):
                temp = ar[j+1]
                ar[j+1] = ar[j]
                ar[j] = temp

    return ar

# Время: худший O(n^2), средний O(n^2), лучший O(n)
# Память: O(1)


def selection_sort(ar):
    """
    Сортировка выбором.
    Находит минимальный элемент в неотсортированной
    части и меняет его с текущим.
    Сложность: худший/средний/лучший O(n^2). Память: O(1).
    """
    for i in range(len(ar)):
        min = 2**100
        min_ind = -1
        for j in range(i, len(ar)):
            if min > ar[j]:
                min = ar[j]
                min_ind = j
        if min_ind != -1:
            temp = ar[i]
            ar[i] = ar[min_ind]
            ar[min_ind] = temp

    return ar

# Время: худший O(n^2), средний O(n^2), лучший O(n^2)
# Память: O(1)


def insertion_sort(ar):
    """
    Сортировка вставками.
    Вставляет каждый элемент на своё место в отсортированной части массива.
    Сложность: худший/средний O(n^2), лучший O(n). Память: O(1).
    """
    for i in range(1, len(ar)):
        key = ar[i]
        j = i - 1
        while j >= 0 and ar[j] > key:
            ar[j + 1] = ar[j]
            j -= 1
        ar[j + 1] = key
    return ar

# Время: худший O(n^2), средний O(n^2), лучший O(n)
# Память: O(1)


def merge_sort(ar):
    """
    Сортировка слиянием.
    Рекурсивно делит массив пополам и сливает отсортированные части.
    Сложность: худший/средний/лучший O(n log n). Память: O(n).
    """
    if len(ar) <= 1:
        return ar
    mid = len(ar) // 2
    left = merge_sort(ar[:mid])
    right = merge_sort(ar[mid:])
    return merge(left, right)

# Время: худший O(n log n), средний O(n log n), лучший O(n log n)
# Память: O(n)


def merge(left, right):
    """
    Сливает два отсортированных массива в один отсортированный.
    Используется в merge_sort.
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(ar):
    """
    Быстрая сортировка (quick sort).
    Делит массив относительно опорного элемента и рекурсивно сортирует части.
    Сложность: худший O(n^2), средний/лучший O(n log n).
    Память: O(log n) (стек рекурсии).
    """
    if len(ar) <= 1:
        return ar
    pivot = ar[len(ar) // 2]
    left = [x for x in ar if x < pivot]
    middle = [x for x in ar if x == pivot]
    right = [x for x in ar if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Время: худший O(n^2), средний O(n log n), лучший O(n log n)
# Память: O(log n) (стек рекурсии)
