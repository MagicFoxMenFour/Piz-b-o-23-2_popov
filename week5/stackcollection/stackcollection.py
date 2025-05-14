import json
from stack import Stack  # Убедитесь, что класс Stack импортирован

class StackCollection:
    """Класс-контейнер для хранения набора объектов Stack."""

    def __init__(self):
        """Инициализация контейнера."""
        self.stacks = []

    def __str__(self):
        """Возвращает строковое представление контейнера."""
        return "\n".join([f"Stack {i}: {stack}" for i, stack in enumerate(self.stacks)])

    def __getitem__(self, index):
        """Возвращает стек по индексу или срезу."""
        return self.stacks[index]

    def add(self, stack):
        """Добавляет стек в контейнер."""
        if not isinstance(stack, Stack):
            raise TypeError("Можно добавлять только объекты класса Stack.")
        self.stacks.append(stack)

    def remove(self, index):
        """Удаляет стек из контейнера по индексу."""
        if 0 <= index < len(self.stacks):
            self.stacks.pop(index)
        else:
            raise IndexError("Индекс вне диапазона.")

    def save(self, filename):
        """Сохраняет контейнер в JSON-файл."""
        with open(filename, 'w') as file:
            json.dump([stack.items for stack in self.stacks], file)

    @classmethod
    def load(cls, filename):
        """Загружает контейнер из JSON-файла."""
        collection = cls()
        with open(filename, 'r') as file:
            data = json.load(file)
            for items in data:
                stack = Stack()
                stack.items = items
                collection.add(stack)
        return collection