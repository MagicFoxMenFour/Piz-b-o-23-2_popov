from WritingInstrument import WritingInstrument

class Pen(WritingInstrument):
    """
    Класс, представляющий ручку.
    Наследует от WritingInstrument и добавляет характеристику типа чернил.
    """
    def __init__(self, color, ink_type):
        super().__init__(color)
        self.ink_type = ink_type

    def write(self, text):
        """
        Пишет указанный текст с использованием ручки.
        Уменьшает износостойкость на 1.
        """
        print(f"Ручка с чернилами типа {self.ink_type} пишет текст '{text}'")
        self._durability -= 1
        print(f"Износостойкость уменьшена до {self._durability}")