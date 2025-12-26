import timeit

from collections import deque
import matplotlib.pyplot as plt
from modules.linked_list import LinkedList


def measure_list_realization(count):
    """
    Измеряет время вставки элементов в начало списка.
    Вычисляет для list и linked_list
    Возвращает: Кортеж из двух элементов
    (list_time, linked_list_time )
    """
    # Тест времени вставки для списка
    test_list = list()
    start1 = timeit.default_timer()
    for i in range(count):
        test_list.insert(0, i)
    end1 = timeit.default_timer()

    # Тест времени вставки для связанного списка
    test_linked_list = LinkedList()
    start2 = timeit.default_timer()
    for i in range(count):
        test_linked_list.insert_at_start(i)
    end2 = timeit.default_timer()
    return ((end1 - start1) * 1000, (end2 - start2) * 1000)


def measure_queue_realization(count):
    """
    Измеряет время реализации очереди.
    Вычисляет для list и deque
    Возвращает: Кортеж из двух элементов
    (list_time, deque_time )
    """
    # Тест списка для реализации очереди
    test_list_queue = list()
    for i in range(count):
        test_list_queue.append(i)

    start1 = timeit.default_timer()
    for i in range(count):
        test_list_queue.pop(0)
    end1 = timeit.default_timer()

    # Тест деки для реализации очереди
    test_deque_queue = deque()
    for i in range(count):
        test_deque_queue.append(i)

    start2 = timeit.default_timer()
    for i in range(count):
        test_deque_queue.popleft()
    end2 = timeit.default_timer()
    return ((end1 - start1) * 1000, (end2 - start2) * 1000)

# Visualuzation block


def Visualization(sizes=[100, 1000, 10000, 100000]):
    """
    Визуализация результатов замеров времени вставки в список
    и реализации очереди.
    Сохраняет графики в папку ОТЧЁТ.
    """
    list_measure = []
    linked_list_measure = []
    for size in sizes:
        measures = measure_list_realization(size)
        list_measure.append(measures[0])
        linked_list_measure.append(measures[1])

    plt.plot(sizes, list_measure, marker="o", color="red", label="list")
    plt.plot(sizes, linked_list_measure, marker="o",
             color="green", label="linked_list")
    plt.xlabel("Количество элементов N")
    plt.ylabel("Время выполнения ms")
    plt.title("Тест времени вставки для списка")
    plt.legend(loc="upper left", title="Collections")
    plt.savefig('./report/time_complexity_plot_list.png',
                dpi=300, bbox_inches='tight')
    plt.show()

    list_queue_measures = []
    deque_measures = []
    for size in sizes:
        measures = measure_list_realization(size)
        list_queue_measures.append(measures[0])
        deque_measures.append(measures[1])

    plt.plot(sizes, list_queue_measures, marker="o", color="red", label="list")
    plt.plot(sizes, deque_measures, marker="o",
             color="green", label="deque")
    plt.xlabel("Количество элементов N")
    plt.ylabel("Время выполнения ms")
    plt.title("Тест времени реализации очереди")
    plt.legend(loc="upper left", title="Collections")
    plt.savefig('./report/time_complexity_plot_queue.png',
                dpi=300, bbox_inches='tight')
    plt.show()

    # Характеристики вычислительной машины
    pc_info = """
    Характеристики ПК для тестирования:
    - Процессор: Intel Core i5-12500H @ 2.50GHz
    - Оперативная память: 32 GB DDR4
    - ОС: Windows 11
    - Python: 3.12
    """
    print(pc_info)
    print(f"{list_measure} - list \n {linked_list_measure} -linked_list \n"
          f"{list_queue_measures} - list \n {deque_measures} - deque")


Visualization()
