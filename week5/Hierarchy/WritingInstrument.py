class WritingInstrument:
    """
    Базовый класс для всех пишущих принадлежностей.
    Содержит общие характеристики и методы.
    """
    def __init__(self, color):
        self.color = color  # Публичное поле
        self._durability = 100  # Защищенное поле
        self.__material = "plastic"  # Приватное поле

    def write(self, text):
        """
        Пишет указанный текст с использованием пишущей принадлежности.
        Уменьшает износостойкость на 1.
        """
        print(f"Пишем текст '{text}' цветом {self.color}")
        self._durability -= 1
        print(f"Износостойкость уменьшена до {self._durability}")

    def _show_material(self):
        """
        Возвращает материал пишущей принадлежности.
        Это защищенный метод.
        """
        return self.__material