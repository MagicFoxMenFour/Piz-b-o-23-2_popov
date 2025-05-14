from WritingInstrument import WritingInstrument

class Pencil(WritingInstrument):
    """
    Класс, представляющий карандаш.
    Наследует от WritingInstrument и добавляет характеристику твердости.
    """
    def __init__(self, color, hardness):
        super().__init__(color)
        self.hardness = hardness

    def write(self, text):
        """
        Пишет указанный текст с использованием карандаша.
        Уменьшает износостойкость на 2.
        """
        print(f"Карандаш с твердостью {self.hardness} пишет текст '{text}'")
        self._durability -= 2
        print(f"Износостойкость уменьшена до {self._durability}")