# heap.py

class Heap():
    """
    Реализация двоичной кучи (min-heap или max-heap).

    Attributes:
        is_min: True — min-куча (минимум в корне), False — max-куча.
        array: Внутренний массив, используемый для представления кучи.
    """

    def __init__(self, is_min=False):
        """
        Инициализирует кучу.

        Args:
            is_min: Булево значение, определяющее тип кучи (min или max).
        """
        self.is_min = is_min
        self.array = []

    # Временная сложность: O(1)

    def insert(self, value):
        """
        Вставляет значение в кучу.

        Args:
            value: Значение для вставки.

        Returns:
            None
        """
        # Вставка элемента
        self.array.append(value)
        self._sift_up(len(self.array) - 1)
    # Временная сложность: O(log n) — всплытие O(log n)

    def extract(self):
        """
        Удаляет и возвращает корневой элемент кучи.
        (max или min в зависимости от типа).

        Returns:
            result: корневой элемент кучи или None, если куча пуста
        """
        if not self.array:
            return None

        if len(self.array) == 1:
            return self.array.pop()

        result = self.array[0]
        # Перемещаем последний элемент в корень
        self.array[0] = self.array.pop()
        if self.array:  # Если в куче остались элементы
            self._sift_down(0)
        return result
    # Временная сложность: O(log n) — погружение O(log n)

    def peek(self):
        """
        Возвращает значение корня кучи без удаления.

        Returns:
            Корневое значение (min или max в зависимости от типа кучи).
        """
        # Просмотр корня
        return self.array[0]

    # Временная сложность: O(1)

    def build_heap(self, array):
        """
        Строит кучу из произвольного массива за линейное время.

        Args:
            array: Список значений, из которого строится куча.

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
            if self.array[index] < self.array[parent_index]:
                self.swap(parent_index, index)
                self._sift_up(parent_index)
        else:
            if self.array[index] > self.array[parent_index]:
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
                if (self.array[left_index] < self.array[index]
                        and self.array[left_index] <= self.array[right_index]):
                    self.swap(index, left_index)
                    self._sift_down(left_index)
                elif (self.array[right_index] < self.array[index]
                        and self.array[right_index] <= self.array[left_index]):
                    self.swap(index, right_index)
                    self._sift_down(right_index)
                else:
                    return
            else:
                if self.array[left_index] < self.array[index]:
                    self.swap(index, left_index)
                    self._sift_down(left_index)
                else:
                    return
        else:
            if right_index is not None:
                if (self.array[left_index] > self.array[index]
                        and self.array[left_index] >= self.array[right_index]):
                    self.swap(index, left_index)
                    self._sift_down(left_index)
                elif (self.array[right_index] > self.array[index]
                        and self.array[right_index] >= self.array[left_index]):
                    self.swap(index, right_index)
                    self._sift_down(right_index)
                else:
                    return
            else:
                if self.array[left_index] > self.array[index]:
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

    def visualize(self, index=0, level=0):
        if not self.array:
            print("Heap is empty")
            return
        if index >= len(self.array):
            return
        # Сначала правое поддерево
        self.visualize(2 * index + 2, level + 1)
        # Текущий узел
        print("    " * level + str(self.array[index]))
        # Потом левое поддерево
        self.visualize(2 * index + 1, level + 1)
