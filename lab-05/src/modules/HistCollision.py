# HistCollision.py

import random
import string
import matplotlib.pyplot as plt
from modules.hash_functions import djb2_hash


class ChainHashTableByCollision:
    """
    Урезанная реализация класса хеш таблицы методом
    цепочек под посчёт распределения
    колизий
    """

    def __init__(self, size=100, hash_func=djb2_hash):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.collisions = []
        self._hash = hash_func

    def insert(self, key):
        """
        Вставляет элемент с ключом и значением в таблицу.
        Если ключ уже существует, обновляет значение.

        Args:
            key: Ключ значения для вставки
            value: Значение для вставки
        """
        index = self._hash(key) % self.size
        chain = self.table[index]
        if len(chain) > 0:
            self.collisions.append(len(chain))  # коллизия
        chain.append(key)
        if sum(len(c) for c in self.table) / self.size > 0.7:
            self._resize()

    def _resize(self):
        """
        Увеличивает размер внутренней таблицы и перераспределяет ключи.
        """
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        for chain in old_table:
            for key in chain:
                self.insert(key)


class LinearProbingHashTableByCollision:
    """
    Урезанная реализация класса хеш таблицы открытой
    адресации с линейной пробацией под посчёт распределения
    колизий
    """

    def __init__(self, size=100, hash_func=djb2_hash):
        self.size = size
        self.table = [None] * size
        self.collisions = []
        self._hash = hash_func

    def insert(self, key):
        """
        Вставляет ключ в таблицу с линейным пробированием.
        При столкновении считает количество шагов до свободной ячейки.

        Args:
            key: Ключ (строка) для вставки.
        """
        index = self._hash(key) % self.size
        start = index
        steps = 0
        while self.table[index] is not None:
            steps += 1
            index = (index + 1) % self.size
            if index == start:
                raise Exception("Таблица переполнена")
        if steps > 0:
            self.collisions.append(steps)
        self.table[index] = key


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


class DoubleHashingHashTableByCollision:
    """
    Урезанная реализация класса хеш таблицы открытой
    адресации с двойным хешированием под посчёт распределения
    колизий
    """

    def __init__(self, size=100, hash_func1=djb2_hash,
                 hash_func2=djb2_hash):
        self.size = next_prime(size)
        self.table = [None] * self.size
        self.collisions = []
        self._hash1 = hash_func1
        self._hash2 = hash_func2

    def insert(self, key):
        """
        Вставляет ключ в таблицу с двойным хешированием.
        Использует вторую хеш-функцию для вычисления шага пробирования.
        При коллизиях фиксирует число шагов до свободной ячейки.

        Args:
            key: Ключ (строка) для вставки.
        """
        checked_ind = []
        index = self._hash1(key) % self.size

        step = self._hash2(key) % (self.size - 1) + 1
        if step % self.size == 0:
            step = 1

        steps = 0
        while self.table[index] is not None:
            steps += 1
            index = (index + step) % self.size
            if index not in checked_ind:
                checked_ind.append(index)
            if len(checked_ind) == self.size:
                raise Exception("Таблица переполнена")
        if steps > 0:
            self.collisions.append(steps)
        self.table[index] = key


def generate_random_string_loop(length):
    """
    Генерирует рандомную строку длины length

    Args:
        length: длина строки для генерации

    Returns:
        random_string: Сгенерированная строка
    """
    characters = string.ascii_letters + string.digits
    random_string = ""
    for _ in range(length):
        random_string += random.choice(characters)
    return random_string


def visualisation(hash_func, N=2000, func_name="table"):
    """
    Собирает данные по распределению колизий и вызывает
    функцию по созданию графиков

    Args:
        hash_func: Хеш функция для которой производится замер
        N: Размер хеш-таблиц и количество элементов
        func_name: Наименование функции для графика
    """

    keys = [generate_random_string_loop(10) for _ in range(N)]

    chain_ht = ChainHashTableByCollision(N//10, hash_func=hash_func)
    linear_ht = LinearProbingHashTableByCollision(N, hash_func=hash_func)
    double_ht = DoubleHashingHashTableByCollision(
        N, hash_func1=hash_func, hash_func2=hash_func)

    for k in keys:
        chain_ht.insert(k)
        linear_ht.insert(k)
        double_ht.insert(k)

    data = [chain_ht, linear_ht, double_ht]

    create_plot(data, "./report/" + func_name + ".png")


def create_plot(data, path):
    """
    Создаёт рисунок по пути path, на котором изображены 3 графика
    зависимости распределения колизий от хеш-функции

    Args:
        data: Списко колизий для постройки гистограммы
        path: Путь для сохранения графика
    """
    plt.figure(figsize=(14, 5))

    plt.subplot(1, 3, 1)
    plt.hist(data[0].collisions, bins=20, edgecolor='black')
    plt.title("Метод цепочек")
    plt.xlabel("Количество коллизий на вставку")
    plt.ylabel("Частота")

    plt.subplot(1, 3, 2)
    plt.hist(data[1].collisions, bins=20, edgecolor='black', color='orange')
    plt.title("Линейное пробирование")
    plt.xlabel("Количество коллизий на вставку")

    plt.subplot(1, 3, 3)
    plt.hist(data[2].collisions, bins=20, edgecolor='black', color='green')
    plt.title("Двойное хеширование")
    plt.xlabel("Количество коллизий на вставку")

    plt.tight_layout()
    plt.savefig(path)
    plt.show()
