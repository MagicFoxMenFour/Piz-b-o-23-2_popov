from collections import deque
import time


def bracket_task(brackets):
    """
    Проверяет, являются ли скобки в строке сбалансированными.
    Поддерживаются круглые, квадратные и фигурные скобки.
    Аргументы:
        brackets: строка со скобками для проверки.
    Возвращает:
        True, если скобки сбалансированы, иначе False.
    """
    balanced = True
    print(brackets.__len__())
    if (brackets.__len__() % 2 == 0):
        for i in range(brackets.__len__() // 2):
            pair = brackets[brackets.__len__() - (1+i)]
            if brackets[i] == "{":
                if (pair != "}"):
                    balanced = False
                    break
            elif brackets[i] == "[":
                if (pair != "]"):
                    balanced = False
                    break
            elif brackets[i] == "(":
                if (pair != ")"):
                    balanced = False
                    break
            else:
                balanced = False
                break
    else:
        balanced = False
    return balanced


def printing_task(orders):
    """
    Моделирует процесс печати документов из очереди.
    Каждый заказ печатается с задержкой в 2 секунды.
    Аргументы:
        orders: итерируемый объект с названиями документов для печати.
    """
    deq = deque(orders)
    print("Начало печати")
    while deq.__len__() != 0:
        time.sleep(2)
        print(f"{deq.popleft()} напечатано")
    print("Конец печати")


def palindrome_task(palindrom):
    """
    Проверяет, является ли переданная последовательность палиндромом.
    Аргументы:
        palindrom: строка или последовательность для проверки.
    Возвращает:
        True, если последовательность палиндром, иначе False.
    """
    deq = deque(palindrom)
    is_palindrom = True
    for i in range(deq.__len__() // 2):
        if (deq[i] != deq[deq.__len__() - (1+i)]):
            is_palindrom = False
            break
    return is_palindrom
