from Pencil import Pencil
from Pen import Pen
from GelPen import GelPen

def main():
    """
    Основная функция для тестирования функциональности пишущих принадлежностей.
    """
    pencil = Pencil("серый", "HB")
    pencil.write("Привет, мир!")

    pen = Pen("синий", "шариковые")
    pen.write("Привет, мир!")

    gel_pen = GelPen("черный", "гелевые", "высокий")
    gel_pen.write("Привет, мир!")

if __name__ == "__main__":
    main()