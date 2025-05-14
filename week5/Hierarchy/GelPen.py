from Pen import Pen

class GelPen(Pen):
    """
    Класс, представляющий гелевую ручку.
    Наследует от Pen и добавляет характеристику блеска.
    """
    def __init__(self, color, ink_type, shimmer):
        super().__init__(color, ink_type)
        self.shimmer = shimmer

    def write(self, text):
        """
        Пишет указанный текст с использованием гелевой ручки.
        Уменьшает износостойкость на 1.
        """
        print(f"Гелевая ручка с блеском {self.shimmer} пишет текст '{text}'")
        self._durability -= 1
        print(f"Износостойкость уменьшена до {self._durability}")