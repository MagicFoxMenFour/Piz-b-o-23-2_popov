import unittest
from src.modules.heap import Heap
from src.modules.heapsort import heapsort, heapsort_in_place
from src.modules.priority_queue import PriorityQueue


class HeapTest(unittest.TestCase):
    def setUp(self):
        # создаём min-кучу и max-кучу для тестов
        self.min_heap = Heap(True)
        self.max_heap = Heap(False)
        # заполняем тестовыми значениями
        values = [50, 30, 70, 20, 40, 60, 80]
        for v in values:
            self.min_heap.insert(v)
            self.max_heap.insert(v)

    def test_min_heap_properties(self):
        # проверка что корень минимальный и извлекаются элементы по возрастанию
        self.assertEqual(self.min_heap.peek(), 20)
        sorted_values = []
        while len(self.min_heap.array) > 0:
            sorted_values.append(self.min_heap.extract())
        self.assertEqual(sorted_values, [20, 30, 40, 50, 60, 70, 80])

    def test_max_heap_properties(self):
        # проверка что корень максимальный и извлекаются элементы по убыванию
        self.assertEqual(self.max_heap.peek(), 80)
        sorted_values = []
        while len(self.max_heap.array) > 0:
            sorted_values.append(self.max_heap.extract())
        self.assertEqual(sorted_values, [80, 70, 60, 50, 40, 30, 20])

    def test_build_heap(self):
        # проверка построения кучи из массива
        test_array = [5, 2, 9, 1, 7, 6, 3]

        # тест для min-heap
        min_heap = Heap(True)
        min_heap.build_heap(test_array.copy())
        self.assertEqual(min_heap.peek(), 1)  # минимум должен быть в корне

        # тест для max-heap
        max_heap = Heap(False)
        max_heap.build_heap(test_array.copy())
        self.assertEqual(max_heap.peek(), 9)  # максимум должен быть в корне


class HeapSortTest(unittest.TestCase):
    def setUp(self):
        self.test_arrays = [
            [5, 2, 9, 1, 7, 6, 3],  # обычный случай
            [1, 2, 3, 4, 5],        # уже отсортированный
            [5, 4, 3, 2, 1],        # обратный порядок
            [1],                     # один элемент
            []                       # пустой массив
        ]

    def test_heapsort(self):
        for arr in self.test_arrays:
            with self.subTest(arr=arr):
                # проверяем обычную сортировку кучей
                sorted_arr = heapsort(arr.copy())
                self.assertEqual(sorted_arr, sorted(arr))

    def test_heapsort_in_place(self):
        for arr in self.test_arrays:
            with self.subTest(arr=arr):
                # проверяем сортировку кучей на месте
                arr_copy = arr.copy()
                heapsort_in_place(arr_copy)
                self.assertEqual(arr_copy, sorted(arr))


class PriorityQueueTest(unittest.TestCase):
    def setUp(self):
        # создаём min и max очереди с приоритетами
        self.min_pq = PriorityQueue(True)
        self.max_pq = PriorityQueue(False)

    def test_priority_queue_operations(self):
        # тестируем операции с min очередью
        items = [(100, 4), (200, 2), (300, 3), (400, 1)]
        for item, priority in items:
            self.min_pq.enqueue(item, priority)

        # проверяем что элементы извлекаются в порядке приоритетов
        self.assertEqual(self.min_pq.dequeue(), 400)  # priority 1
        self.assertEqual(self.min_pq.dequeue(), 200)  # priority 2
        self.assertEqual(self.min_pq.dequeue(), 300)  # priority 3
        self.assertEqual(self.min_pq.dequeue(), 100)  # priority 4

    def test_priority_queue_build(self):
        # тест построения очереди из массива пар (элемент, приоритет)
        items = [(100, 4), (200, 2), (300, 3), (400, 1)]

        # тест для min очереди
        self.min_pq.build_queue(items.copy())
        results = []
        while len(self.min_pq.array) > 0:
            results.append(self.min_pq.dequeue())
        self.assertEqual(results, [400, 200, 300, 100])

        # тест для max очереди
        self.max_pq.build_queue(items.copy())
        results = []
        while len(self.max_pq.array) > 0:
            results.append(self.max_pq.dequeue())
        self.assertEqual(results, [100, 300, 200, 400])


# if __name__ == '__main__':
#     unittest.main()
