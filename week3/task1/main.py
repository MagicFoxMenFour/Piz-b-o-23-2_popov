class Roman:
    """
    Класс Roman представляет римское число и поддерживает основные арифметические операции.
    """

    _roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    _int_to_roman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 
                     90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}

    def __init__(self, value: str):
        """
        Инициализация объекта Roman.

        :param value: Строка, представляющая римское число.
        """
        self.value = value

    @staticmethod
    def to_int(roman: str) -> int:
        """
        Преобразует римское число в целое число.

        :param roman: Строка, представляющая римское число.
        :return: Целое число.
        """
        total = 0
        prev_value = 0
        for char in reversed(roman):
            value = Roman._roman_to_int[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total

    @staticmethod
    def to_roman(num: int) -> str:
        """
        Преобразует целое число в римское число.

        :param num: Целое число.
        :return: Строка, представляющая римское число.
        """
        result = ''
        for value, symbol in sorted(Roman._int_to_roman.items(), reverse=True):
            while num >= value:
                result += symbol
                num -= value
        return result

    def __add__(self, other: 'Roman') -> 'Roman':
        """
        Сложение двух римских чисел.

        :param other: Другое римское число.
        :return: Новое римское число, представляющее сумму.
        """
        num1 = self.to_int(self.value)
        num2 = self.to_int(other.value)
        return Roman(self.to_roman(num1 + num2))

    def __sub__(self, other: 'Roman') -> 'Roman':
        """
        Вычитание двух римских чисел.

        :param other: Другое римское число.
        :return: Новое римское число, представляющее разность.
        """
        num1 = self.to_int(self.value)
        num2 = self.to_int(other.value)
        return Roman(self.to_roman(num1 - num2))

    def __mul__(self, other: 'Roman') -> 'Roman':
        """
        Умножение двух римских чисел.

        :param other: Другое римское число.
        :return: Новое римское число, представляющее произведение.
        """
        num1 = self.to_int(self.value)
        num2 = self.to_int(other.value)
        return Roman(self.to_roman(num1 * num2))

    def __truediv__(self, other: 'Roman') -> 'Roman':
        """
        Деление двух римских чисел.

        :param other: Другое римское число.
        :return: Новое римское число, представляющее частное.
        """
        num1 = self.to_int(self.value)
        num2 = self.to_int(other.value)
        return Roman(self.to_roman(num1 // num2))

    def __str__(self) -> str:
        """
        Возвращает строковое представление римского числа.

        :return: Строка, представляющая римское число.
        """
        return self.value

# Пример использования
r1 = Roman("X")
r2 = Roman("V")
print(f"{r1} + {r2} = {r1 + r2}")  # XV
print(f"{r1} - {r2} = {r1 - r2}")  # V
print(f"{r1} * {r2} = {r1 * r2}")  # L
print(f"{r1} / {r2} = {r1 / r2}")  # II