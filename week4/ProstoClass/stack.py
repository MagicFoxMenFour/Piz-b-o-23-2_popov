import json

class Stack:
    """Класс для работы со стеком."""

    def __init__(self):
        """Инициализация стека."""
        self.items = []

    def __str__(self):
        """Возвращает строковое представление стека."""
        return str(self.items)

    def push(self, item):
        """Добавляет элемент в стек."""
        self.items.append(item)

    def pop(self):
        """Удаляет и возвращает верхний элемент стека."""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Попытка извлечь элемент из пустого стека")

    def is_empty(self):
        """Проверяет, пуст ли стек."""
        return len(self.items) == 0

    def peek(self):
        """Возвращает верхний элемент стека без его удаления."""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Попытка получить элемент из пустого стека")

    def size(self):
        """Возвращает количество элементов в стеке."""
        return len(self.items)

    def save(self, filename):
        """Сохраняет стек в JSON-файл."""
        with open(filename, 'w') as file:
            json.dump(self.items, file)

    @classmethod
    def load(cls, filename):
        """Загружает стек из JSON-файла."""
        stack = cls()
        with open(filename, 'r') as file:
            stack.items = json.load(file)
        return stack