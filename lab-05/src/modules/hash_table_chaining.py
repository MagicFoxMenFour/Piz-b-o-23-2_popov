# hash_table_chaining.py

from modules.hash_functions import polynomial_hash
# from src.modules.hash_functions import polynomial_hash  # by test


class Node:
    """
    Класс узла односвязного списка.

    Attributes:
        key: Ключ элемента.
        value: Значение элемента.
        next: Ссылка на следующий узел в цепочке.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class ChainingHashTable:
    """
    Класс хеш-таблицы методом цепочек с динамическим масштабированием.
    Поддерживает вставку, поиск и удаление элементов.


    """

    def __init__(self, initial_size=8, load=0.7, hash_func=polynomial_hash):
        """
        Инициализация хеш-таблицы.

         Args:
            initial_size : Начальный размер внутреннего массива;
            load : Порог коэффициента заполнения.
            hash_func : Функция хеширования.
        """
        self.size = initial_size
        self.count = 0
        self.table = [None] * self.size
        self.min_size = 8
        self.load = load
        self._hash = hash_func

    def _resize(self):
        """
        Увеличивает размер таблицы вдвое при превышении порога загрузки.
        Перераспределяет все элементы в новые индексы.
        """
        old_table = self.table
        self.size *= 2
        self.table = [None] * self.size
        self.count = 0
        for node in old_table:
            current = node
            while current:
                self.insert(current.key, current.value)
                current = current.next
    # Временная сложность: O(n) — перераспределение всех элементов
    # Пространственная сложность: O(1) — перераспределение
    # происходит in-place

    def _shrink(self):
        """
        Уменьшает размер таблицы вдвое при низкой загрузке (не меньше min_size)
        Перераспределяет все элементы в новые индексы.
        """
        old_table = self.table
        self.size = max(self.min_size, self.size // 2)
        self.table = [None] * self.size
        self.count = 0
        for node in old_table:
            current = node
            while current:
                self.insert(current.key, current.value)
                current = current.next
    # Временная сложность: O(n) — перераспределение всех элементов
    # Пространственная сложность: O(1) — используется константное
    # дополнительное пространство

    def insert(self, key, value):
        """
        Вставляет элемент с ключом и значением в таблицу.
        Если ключ уже существует, обновляет значение.
        Args:
            key: Ключ элемента.
            value: Значение элемента.

        Returns:
            None
        """
        if self.count / self.size > self.load:
            self._resize()
        index = self._hash(key) % self.size
        head = self.table[index]
        current = head
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next
        new_node = Node(key, value)
        new_node.next = head
        self.table[index] = new_node
        self.count += 1
    # Временная сложность: среднее O(1), худшее O(n)
    # при длинной цепочке или при resize
    # Пространственная сложность: O(1) — добавляется один узел

    def get(self, key):
        """
        Возвращает значение элемента по ключу.
        Args:
            key: Ключ элемента.
        Returns:
            Значение элемента, либо None, если ключ не найден.
        """
        index = self._hash(key) % self.size
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
        # Временная сложность: среднее O(1), худшее O(n) при коллизиях
        # Пространственная сложность: O(1)

    def remove(self, key):
        """
        Удаляет элемент по ключу.

        Args:
            key: Ключ элемента для удаления.

        Returns:
            True, если элемент удалён, иначе False.
        """
        index = self._hash(key) % self.size
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                self.count -= 1
                if self.size > self.min_size and self.count / self.size < 0.25:
                    self._shrink()
                return True
            prev = current
            current = current.next
        return False
        # Временная сложность: среднее O(1), худшее O(n) при длинной цепочке
        # Пространственная сложность: O(1)

    def display(self):
        """
        Выводит текущее состояние таблицы для отладки.
        Показывает все цепочки в таблице.
        """
        for i, node in enumerate(self.table):
            print(f"Bucket {i}:", end=" ")
            current = node
            while current:
                print(f"({current.key}: {current.value})", end=" -> ")
                current = current.next
            print("None")
