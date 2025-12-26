# priority_queue.py

class PriorityQueue():

    def __init__(self, is_min=False):
        """
        Инициализирует приоритетную очередь.

        Args:
            is_min: Булево значение, определяющее тип приоритета (min или max).
        """
        self.array = []
        self.is_min = is_min
    # Временная сложность: O(1)

    def enqueue(self, item, priority):
        """
        Вставляет значение в приоритетную очередь.

        Args:
            value: Значение для вставки.

        Returns:
            None
        """
        # Вставка элемента
        self.array.append((item, priority))
        self._sift_up(len(self.array) - 1)
    # Временная сложность: O(log n) — всплытие O(log n)

    def dequeue(self):
        """
        Удаляет и выводит элемент приоритетной очереди.
        (max или min в зависимости от типа).

        Returns:
            Значение элемента в очереди
        """
        # Извлечение корня
        self.swap(0, len(self.array) - 1)
        result = self.array.pop(len(self.array) - 1)
        self._sift_down(0)
        return result[0]
    # Временная сложность: O(log n) — погружение O(log n)

    def build_queue(self, array):
        """
        Строит приоритетную очередь из произвольного массива за линейное время.

        Args:
            array: Список значений, из которого строится приоритетная очередь.

        Returns:
            None
        """
        # Построение кучи из массива
        self.array = array
        parents_start_index = (len(array) - 2) // 2
        for i in range(parents_start_index, -1, -1):
            self._sift_down(i)
    # Временная сложность: O(n) — построение кучи снизу вверх за линейное время

    def _sift_up(self, index):
        """
        Выполняет всплытие элемента вверх по дереву
        до восстановления свойства кучи.

        Args:
            index: Индекс элемента во внутреннем массиве,
                который нужно всплыть.

        Returns:
            None
        """
        # Всплытие элемента (Insert)
        if index == 0:
            return
        parent_index = (index - 1) // 2

        if self.is_min:
            if self.array[index][1] < self.array[parent_index][1]:
                self.swap(parent_index, index)
                self._sift_up(parent_index)
        else:
            if self.array[index][1] > self.array[parent_index][1]:
                self.swap(parent_index, index)
                self._sift_up(parent_index)

    # Временная сложность: O(log n) — перемещение вверх по высоте кучи

    def _sift_down(self, index):
        """
        Выполняет погружение элемента вниз по дереву
        до восстановления свойства кучи.

        Args:
            index: Индекс элемента во внутреннем массиве,
                который нужно погрузить.

        Returns:
            None
        """
        # Погружение элемента (Extract)
        left_index = 2*index + 1
        right_index = 2 * index + 2
        if left_index > (len(self.array) - 1):
            left_index = None
        if right_index > (len(self.array) - 1):
            right_index = None
        if left_index is None and right_index is None:
            return
        if self.is_min:
            if right_index is not None:
                if (self.array[left_index][1] < self.array[index][1]
                    and (self.array[left_index][1] <
                         self.array[right_index][1])):
                    self.swap(index, left_index)
                    self._sift_down(left_index)
                elif (self.array[right_index][1] < self.array[index][1]
                        and (self.array[right_index][1] <
                             self.array[left_index][1])):
                    self.swap(index, right_index)
                    self._sift_down(right_index)
                else:
                    return
            else:
                if self.array[left_index][1] < self.array[index][1]:
                    self.swap(index, left_index)
                    self._sift_down(left_index)
                else:
                    return
        else:
            if right_index is not None:
                if (self.array[left_index][1] > self.array[index][1]
                        and (self.array[left_index][1] >
                             self.array[right_index][1])):
                    self.swap(index, left_index)
                    self._sift_down(left_index)
                elif (self.array[right_index][1] > self.array[index][1]
                        and (self.array[right_index][1] >
                             self.array[left_index][1])):
                    self.swap(index, right_index)
                    self._sift_down(right_index)
                else:
                    return
            else:
                if self.array[left_index][1] > self.array[index][1]:
                    self.swap(index, left_index)
                    self._sift_down(left_index)
                else:
                    return

    # Временная сложность: O(log n) — перемещение вниз по высоте кучи

    def swap(self, first_index, second_index):
        """
        Меняет местами два элемента внутреннего массива по индексам.

        Args:
            first_index: Индекс первого элемента.
            second_index: Индекс второго элемента.

        Returns:
            None
        """
        temp = self.array[first_index]
        self.array[first_index] = self.array[second_index]
        self.array[second_index] = temp
