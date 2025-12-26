# heapsort.py

from modules.heap import Heap
# from src.modules.heap import Heap
# С выделением памяти под кучу


def heapsort(array):
    """
    Создаёт кучу на основе массива и посредством операции
    excract создаёт отсортированный массив

    Args:
        array: Неотсортированный массив

    Returns:
        sorted_array: Отсортированный массив
    """
    if not array:
        return []

    heap = Heap(False)  # max-куча
    heap.build_heap(array.copy())  # явное копирование
    sorted_array = [0] * len(array)  # предварительное выделение памяти

    for i in range(len(array)-1, -1, -1):
        val = heap.extract()
        if val is None:  # защита от None
            break
        sorted_array[i] = val

    return sorted_array

# Без выделения доп. памяти. Изменение исходного массива


def heapsort_in_place(array):
    """
    Сортирует массив на месте, используя методы кучи.
    Сначала изменяет данные таким образом, чтобы массив стал кучей,
    потом по ставит наибольший элемент в конец, и опять восстанавливает
    кучу без учёта последнего элемента

    Args:
        array: Неотсортированный массив

    Returns:
        None
    """
    def swap(i, j):
        array[i], array[j] = array[j], array[i]

    def _sift_down(index, heap_size):
        largest = index
        while True:
            left = 2 * index + 1
            right = 2 * index + 2

            if left < heap_size and array[left] > array[largest]:
                largest = left
            if right < heap_size and array[right] > array[largest]:
                largest = right

            if largest == index:
                break

            swap(index, largest)
            index = largest

    # Построение max-кучи
    for i in range(len(array) // 2 - 1, -1, -1):
        _sift_down(i, len(array))

    # Извлечение элементов
    for i in range(len(array) - 1, 0, -1):
        swap(0, i)
        _sift_down(0, i)

    return array
