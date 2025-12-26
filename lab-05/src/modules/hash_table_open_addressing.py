# hash_table_open_addressing.py

from modules.hash_functions import polynomial_hash, djb2_hash
# from src.modules.hash_functions import polynomial_hash, djb2_hash


class LinearHashTable:
    """
    Класс хеш-таблицы с открытой адресацией и линейным пробированием.
    Поддерживает вставку, поиск и удаление элементов.
    """

    def __init__(self, size=8, load=0.7, hash_func=polynomial_hash):
        """
        Инициализация хеш-таблицы.

        Args:
            initial_size : Начальный размер внутреннего массива;
            load : Порог коэффициента заполнения.
            hash_func : Функция хеширования.
        """
        self.size = size
        self.table = [None] * size
        self.count = 0
        self.load = load
        self._hash = hash_func

    def _probe(self, key, for_insert=False):
        """
        Линейное пробирование для поиска индекса ключа или свободной ячейки.
        Args:
            key: Ключ элемента.
            for_insert: Если True, ищем первую свободную ячейку или
                        ячейку с этим ключом;
                        если False, ищем существующий ключ.

        Returns:
            Индекс найденной ячейки или None,
            если ключ не найден (for_insert=False).

        """
        index = self._hash(key) % self.size
        start_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return index
            index = (index + 1) % self.size
            if index == start_index:
                break
        if for_insert:
            return index
        return None
        # Временная сложность: среднее O(1), худшее O(n)
        # Пространственная сложность: O(1)

    def insert(self, key, value):
        """
        Вставляет элемент с ключом и значением в таблицу.
        Если ключ уже существует, обновляет значение.
        Args:
            key: Ключ элемента.
            value: Значение элемента.
        """
        if self.count >= self.size * self.load:
            self._resize()
        index = self._probe(key, for_insert=True)
        if self.table[index] is None:
            self.count += 1
        self.table[index] = (key, value)
        # Временная сложность: среднее O(1), худшее O(n) при долгой цепочке
        # Пространственная сложность: O(1)

    def get(self, key):
        """
        Возвращает значение элемента по ключу.
        Args:
            key: Ключ элемента.
        Returns:
            Значение элемента, либо None, если ключ не найден.
        """
        index = self._probe(key)
        if index is not None:
            return self.table[index][1]
        return None
        # Временная сложность: среднее O(1), худшее O(n) при коллизиях
        # Пространственная сложность: O(1)

    def remove(self, key):
        """
        Удаляет элемент по ключу и перехеширует затронутые элементы.
        Args:
            key: Ключ элемента для удаления.
        Returns:
            True, если элемент удалён, иначе False.
        """
        index = self._probe(key)
        if index is not None:
            self.table[index] = None
            self.count -= 1
            self._rehash(index)
            return True
        return False
        # Временная сложность: среднее O(1), худшее O(n)
        # Пространственная сложность: O(1)

    def _rehash(self, empty_index):
        """
        Перехеширование элементов после удаления для линейного пробирования.

        Args:
            empty_index: Индекс только что освободившейся ячейки.
        """
        index = (empty_index + 1) % self.size
        while self.table[index] is not None:
            key, value = self.table[index]
            self.table[index] = None
            self.count -= 1
            self.insert(key, value)
            index = (index + 1) % self.size
        # Временная сложность: O(n) в худшем случае (перехеширование цепочки)
        # Пространственная сложность: O(1)

    def _resize(self):
        """
        Увеличивает размер таблицы вдвое и перераспределяет все элементы.
        """
        old_table = self.table
        self.size *= 2
        self.table = [None] * self.size
        self.count = 0
        for item in old_table:
            if item is not None:
                self.insert(*item)
        # Временная сложность: O(n) — перераспределение всех элементов
        # Пространственная сложность: O(1)

    def display(self):
        """
        Выводит текущее состояние таблицы для отладки.
        Показывает все элементы с их индексами.
        """
        for i in range(self.size):
            if self.table[i] is None:
                print(f"{i}) {None}")
            else:
                print(f"{i}) {self.table[i][0]}: {self.table[i][1]}")
        # Временная сложность: O(n) — проход по всей таблице
        # Пространственная сложность: O(1)


def next_prime(n):
    """
    Возвращает простое число >= n.

    Args:
        n: число больше которого выбирают простое.

    Returns:
        n: Возвращает простое число большее n
    """
    def is_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    while not is_prime(n):
        n += 1
    return n


class DoubleHashingHashTable:
    """
    Класс хеш-таблицы с открытой адресацией и двойным хешированием.
    Поддерживает вставку, поиск и удаление элементов.
    """

    def __init__(self, size=7, load=0.7, hash_func1=polynomial_hash,
                 hash_func2=djb2_hash):
        """
        Инициализация хеш-таблицы.
        Args:
            initial_size : Начальный размер внутреннего массива;
            load : Порог коэффициента заполнения.
            hash_func1 : Функция хеширования значений.
            hash_func2 : Функция хеширования шага пробирования
        """
        self.size = next_prime(size)  # размер таблицы — простое число
        self.table = [None] * self.size
        self.count = 0
        self.load = load
        self._hash1 = hash_func1
        self._hash2 = hash_func2

    def _probe(self, key, for_insert=False):
        """
        Двойное хеширование для поиска индекса ключа или свободной ячейки.

        Args:
            key: Ключ значения.
            for_insert: Переменная-флаг на вставку.
        """
        index = self._hash1(key) % self.size

        # step не должен быть кратен size
        step = self._hash2(key) % (self.size - 1) + 1
        if step % self.size == 0:
            step = 1

        start_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return index
            index = (index + step) % self.size
            if index == start_index:
                break

        if for_insert:
            return index
        return None

    def insert(self, key, value):
        """
        Вставляет элемент с ключом и значением в таблицу.
        Если ключ уже существует, обновляет значение.

        Args:
            key: Ключ значения для вставки
            value: Значение для вставки
        """
        if self.count >= self.size * self.load:
            self._resize()

        index = self._probe(key, for_insert=True)
        if self.table[index] is None:
            self.count += 1
        self.table[index] = (key, value)
        # Временная сложность: среднее O(1), худшее O(n)
        # Пространственная сложность: O(1)

    def get(self, key):
        """
        Возвращает значение элемента по ключу.

        Args:
            key: ключ значения для получения
        """
        index = self._probe(key)
        if index is not None:
            return self.table[index][1]
        return None
        # Временная сложность: среднее O(1), худшее O(n)
        # Пространственная сложность: O(1)

    def remove(self, key):
        """
        Удаляет элемент по ключу и полностью перехеширует таблицу.

        Args:
            key: Ключ значения для удаления.
        """
        index = self._probe(key)
        if index is not None:
            self.table[index] = None
            self.count -= 1
            self._rehash()
            return True
        return False
        # Временная сложность: среднее O(1), худшее O(n)
        # Пространственная сложность: O(1)

    def _rehash(self):
        """
        Перехеширование всех элементов таблицы после удаления.
        """
        old_table = self.table
        self.table = [None] * self.size
        self.count = 0
        for item in old_table:
            if item is not None:
                key, value = item
                self.insert(key, value)
        # Временная сложность: O(n) — восстановление всех элементов
        # Пространственная сложность: O(1)

    def _resize(self):
        """
        Увеличивает размер таблицы до следующего простого числа
        и перераспределяет все элементы.
        """
        old_table = self.table
        self.size = next_prime(self.size * 2)
        self.table = [None] * self.size
        self.count = 0
        for item in old_table:
            if item is not None:
                self.insert(*item)
        # Временная сложность: O(n) — перераспределение всех элементов
        # Пространственная сложность: O(1)

    def display(self):
        """
        Выводит текущее состояние таблицы для отладки.
        """
        for i in range(self.size):
            if self.table[i] is None:
                print(f"{i}) {None}")
            else:
                print(f"{i}) {self.table[i][0]}: {self.table[i][1]}")
