from abc import ABC, abstractmethod

class Pizza(ABC):
    """
    Абстрактный базовый класс для всех видов пицц.
    """
    def __init__(self, name, dough, sauce, toppings):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings

    def prepare(self):
        """
        Подготовка пиццы: замес теста, добавление соуса и начинки.
        """
        print(f"Готовим {self.name}")
        print(f"Замешиваем тесто: {self.dough}")
        print(f"Добавляем соус: {self.sauce}")
        print(f"Добавляем начинку: {', '.join(self.toppings)}")

    def bake(self):
        """
        Выпечка пиццы.
        """
        print("Выпекаем пиццу...")

    def cut(self):
        """
        Нарезка пиццы.
        """
        print("Режем пиццу...")

    def pack(self):
        """
        Упаковка пиццы.
        """
        print("Упаковываем пиццу...")

    @abstractmethod
    def get_cost(self):
        """
        Возвращает стоимость пиццы.
        """
        pass

class PepperoniPizza(Pizza):
    """
    Класс для пиццы Пепперони.
    """
    def __init__(self):
        super().__init__("Пепперони", "тонкое тесто", "томатный соус", ["пепперони", "сыр моцарелла"])

    def get_cost(self):
        return 10

class BarbecuePizza(Pizza):
    """
    Класс для пиццы Барбекю.
    """
    def __init__(self):
        super().__init__("Барбекю", "толстое тесто", "соус барбекю", ["курица", "лук", "сыр моцарелла"])

    def get_cost(self):
        return 12

class SeafoodPizza(Pizza):
    """
    Класс для пиццы Дары Моря.
    """
    def __init__(self):
        super().__init__("Дары Моря", "тонкое тесто", "сливочный соус", ["креветки", "мидии", "сыр моцарелла"])

    def get_cost(self):
        return 15

class Order:
    """
    Класс для заказа, содержащий список пицц.
    """
    def __init__(self):
        self.pizzas = []

    def add_pizza(self, pizza: Pizza):
        """
        Добавляет пиццу в заказ.

        :param pizza: Пицца для добавления в заказ.
        """
        self.pizzas.append(pizza)

    def calculate_total(self):
        """
        Подсчитывает общую стоимость заказа.

        :return: Общая стоимость заказа.
        """
        return sum(pizza.get_cost() for pizza in self.pizzas)

    def display_order(self):
        """
        Отображает информацию о заказе.
        """
        print("Ваш заказ:")
        for pizza in self.pizzas:
            print(f"- {pizza.name}")
        print(f"Общая стоимость: {self.calculate_total()} руб.")

class Terminal:
    """
    Класс для терминала, взаимодействующего с пользователем.
    """
    def __init__(self):
        self.menu = {
            1: PepperoniPizza(),
            2: BarbecuePizza(),
            3: SeafoodPizza()
        }

    def display_menu(self):
        """
        Отображает меню пицц.
        """
        print("Меню:")
        for key, pizza in self.menu.items():
            print(f"{key}. {pizza.name} - {pizza.get_cost()} руб.")

    def take_order(self):
        """
        Принимает заказ от пользователя.
        """
        order = Order()
        while True:
            self.display_menu()
            choice = input("Выберите номер пиццы (или 'готово' для завершения): ")
            if choice.lower() == 'готово':
                break
            try:
                pizza = self.menu[int(choice)]
                order.add_pizza(pizza)
                print(f"Пицца {pizza.name} добавлена в заказ.")
            except (KeyError, ValueError):
                print("Неверный выбор. Пожалуйста, попробуйте снова.")
        order.display_order()
        print("Спасибо за ваш заказ!")

# Пример использования
terminal = Terminal()
terminal.take_order()