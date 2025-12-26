# perfomance_test.py

import timeit
import modules.sorts as sorts
import modules.generate_data as gen_data
import matplotlib.pyplot as plt


def perf_test(gen_data, sizes):
    """
    Запускает тестирование производительности всех сортировок на данных,
    сгенерированных функцией gen_data, для каждого размера из sizes.
    Аргументы:
        gen_data: функция-генератор данных (например, generate_random_data).
        sizes: список целых чисел — размеры тестируемых массивов.
    Возвращает:
        Словарь, где ключ — название метода сортировки, значение — список
        времени выполнения (мс) для каждого размера.
    """

    data = {}
    for size in sizes:
        data[size] = gen_data(size)

    measures = {"bubble sort": measure_time(data, sorts.bubble_sort),
                "select sort": measure_time(data, sorts.selection_sort),
                "insert sort": measure_time(data, sorts.insertion_sort),
                "merge sort": measure_time(data, sorts.merge_sort),
                "quick sort": measure_time(data, sorts.quick_sort)}
    return measures


def measure_time(data, function):
    """
    Измеряет время выполнения сортировки для каждого массива из data.
    Аргументы:
        data: словарь {размер: массив}.
        function: функция сортировки (например, bubble_sort).
    Возвращает:
        Список времени выполнения (мс) для каждого массива.
    """
    measures = []
    for ar in data.values():
        ar_copy = ar.copy()
        start = timeit.default_timer()
        function(ar_copy)
        end = timeit.default_timer()
        measures.append((end-start) * 1000)

    return measures


def Visualization(sizes):
    """
    Строит и сохраняет графики сравнения всех методов сортировки
    на разных типах данных и размерах.
    Аргументы:
        sizes: список целых чисел — размеры тестируемых массивов.
    Возвращает:
        None. Сохраняет графики в папку ОТЧЁТ и отображает их на экране.
    """
    random_data_measures = perf_test(gen_data.generate_random_data, sizes)
    sorted_data_measures = perf_test(gen_data.generate_sorted_data, sizes)
    reversed_data_measures = perf_test(gen_data.generate_reversed_data, sizes)
    almost_sorted_data_measures = perf_test(
        gen_data.generate_almost_sorted_data, sizes)

    Create_plot(random_data_measures, sizes,
                "Сравнение методов сортировки на рандомных данных",
                "./report/random_data_all_methods.png")
    Create_plot(sorted_data_measures, sizes,
                "Сравнение методов сортировки на отсортированных данных",
                "./report/sorted_data_all_methods.png")
    Create_plot(reversed_data_measures, sizes,
                "Сравнение методов сортировки на реверсных данных",
                "./report/reversed_data_all_methods.png")
    Create_plot(almost_sorted_data_measures, sizes,
                "Сравнение методов сортировки на почти отсортированных данных",
                "./report/almost_sorted_data_all_methods.png")


def Create_plot(data, sizes, title, path):
    """
    Строит и сохраняет график времени работы сортировок для одного типа данных.
    Аргументы:
        data: словарь {название метода: список времени}.
        sizes: список размеров массивов.
        title: строка — заголовок графика.
        path: строка — путь для сохранения PNG-файла.
    Возвращает:
        None. Сохраняет график и отображает его.
    """
    plt.plot(sizes, data["bubble sort"],
             marker="o", color="red", label="bubble",)
    plt.plot(sizes, data["select sort"],
             marker="o", color="green", label="select",)
    plt.plot(sizes, data["insert sort"],
             marker="o", color="blue", label="insert",)
    plt.plot(sizes, data["merge sort"],
             marker="o", color="purple", label="merge",)
    plt.plot(sizes, data["quick sort"],
             marker="o", color="brown", label="quick",)
    plt.xlabel("Размер массива n")
    plt.ylabel("Время выполнения ms")
    plt.title(title)
    plt.legend(loc="upper left", title="Методы")
    plt.savefig(path, dpi=300, bbox_inches="tight")
    plt.show()

# , path_csv="./ОТЧЁТ/summary.csv"


def Create_summary_table(sizes):
    """
    Формирует и выводит сводную таблицу результатов тестирования сортировок
    для всех типов данных и размеров.
    Аргументы:
        sizes: список целых чисел — размеры тестируемых массивов.
    Возвращает:
        None. Печатает таблицу в консоль
    """
    # Характеристики вычислительной машины
    pc_info = """
    Характеристики ПК для тестирования:
    - Процессор: Intel Core i5-12500H @ 2.50GHz
    - Оперативная память: 32 GB DDR4
    - ОС: Windows 11
    - Python: 3.12
    """
    print(pc_info)
    generators = {
        "random": gen_data.generate_random_data,
        "sorted": gen_data.generate_sorted_data,
        "reversed": gen_data.generate_reversed_data,
        "almost_sorted": gen_data.generate_almost_sorted_data,
    }

    # вычисление измерений для всех типов данных
    all_measures = {}
    for name, gen in generators.items():
        all_measures[name] = perf_test(gen, sizes)

    # Подгодовка csv линий
    # import csv
    csv_rows = [("data_type", "size", "method", "time_ms")]
    methods = [
        "bubble sort",
        "select sort",
        "insert sort",
        "merge sort",
        "quick sort",
    ]

    for data_type, measures in all_measures.items():
        for i, size in enumerate(sizes):
            for method in methods:
                time_ms = measures[method][i]
                csv_rows.append((data_type, size, method, f"{time_ms:.6f}"))

    # Создание csv файла
    # import os
    # os.makedirs(os.path.dirname(path_csv), exist_ok=True)
    # with open(path_csv, "w", newline='', encoding='utf-8') as f:
    #     writer = csv.writer(f)
    #     writer.writerows(csv_rows)

    # Вывод таблицы в консоль
    col_widths = [max(len(str(r[i])) for r in csv_rows) for i in range(4)]
    sep = " | "
    header = csv_rows[0]
    print(sep.join(str(header[i]).ljust(col_widths[i]) for i in range(4)))
    print('-' * (sum(col_widths) + 3 * (len(col_widths) - 1)))
    for row in csv_rows[1:]:
        print(sep.join(str(row[i]).ljust(col_widths[i]) for i in range(4)))

    # print(f"\nSummary CSV written to: {path_csv}")
