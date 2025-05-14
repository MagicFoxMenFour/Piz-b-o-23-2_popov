from abc import ABC, abstractmethod

class Movable(ABC):
    """
    Абстрактный базовый класс для объектов, которые могут перемещаться.
    """
    @abstractmethod
    def move(self, commands: str) -> list:
        """
        Абстрактный метод для перемещения объекта.

        :param commands: Строка команд для перемещения.
        :return: Список с конечными координатами объекта.
        """
        pass

class Position:
    """
    Класс для представления координат на плоскости.
    """
    def __init__(self, x: int, y: int):
        """
        Инициализация объекта Position.

        :param x: Координата по оси X.
        :param y: Координата по оси Y.
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Возвращает строковое представление координат.

        :return: Строка в формате "(x, y)".
        """
        return f"({self.x}, {self.y})"

class Robot(Movable):
    """
    Класс, представляющий робота, который может перемещаться по плоскости.
    """
    def __init__(self, x: int, y: int):
        """
        Инициализация робота с начальными координатами.

        :param x: Начальная координата по оси X (должна быть от 0 до 100).
        :param y: Начальная координата по оси Y (должна быть от 0 до 100).
        :raises ValueError: Если координаты выходят за пределы допустимого диапазона.
        """
        if not (0 <= x <= 100 and 0 <= y <= 100):
            raise ValueError("Coordinates must be between 0 and 100")
        self._position = Position(x, y)  # Текущее положение робота
        self._path = [Position(x, y)]    # Список для хранения пути робота
        self._step_count = 0              # Приватное поле для отслеживания количества шагов

    def _update_step_count(self):
        """
        Приватный метод для обновления счетчика шагов.
        """
        self._step_count += 1

    def move(self, commands: str) -> list:
        """
        Перемещает робота согласно переданным командам.

        :param commands: Строка команд, где каждая буква (N, S, E, W) указывает направление движения.
        :return: Список с конечными координатами робота [x, y].
        """
        for command in commands:
            new_x, new_y = self._position.x, self._position.y
            if command == 'N' and self._position.y < 100:
                new_y += 1
            elif command == 'S' and self._position.y > 0:
                new_y -= 1
            elif command == 'E' and self._position.x < 100:
                new_x += 1
            elif command == 'W' and self._position.x > 0:
                new_x -= 1

            if (new_x != self._position.x or new_y != self._position.y):
                self._position = Position(new_x, new_y)
                self._path.append(self._position)
                self._update_step_count()  # Обновляем счетчик шагов

        return [self._position.x, self._position.y]

    def path(self) -> list:
        """
        Возвращает путь, который прошел робот с момента последнего вызова метода move.

        :return: Список кортежей с координатами пути [(x1, y1), (x2, y2), ...].
        """
        return [(pos.x, pos.y) for pos in self._path]

    def get_step_count(self) -> int:
        """
        Возвращает количество шагов, сделанных роботом.

        :return: Количество шагов.
        """
        return self._step_count


robot = Robot(50, 50)
print(robot.move("NNEE")) 
print(robot.path())       
print(robot.get_step_count())  