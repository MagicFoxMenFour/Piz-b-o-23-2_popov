# memoization.py
import timeit
import matplotlib.pyplot as plt

# Глобальная переменная для подсчёта числа рекурсивных вызовов
fib_memo_calls = 0
fib_calls = 0


def naive_fibbonachi(n):
    """
    Вычисляет n-ое число Фибоначчи рекурсивно.
    Аргументы:
        n: целое число (индекс) — позиция числа Фибоначчи в последовательности.
    Возвращает:
        n-ое число Фибоначчи
        -1 для некорректных (неположительных) аргументов.
    """
    global fib_calls
    fib_calls += 1
    if n > 0 and n < 3:
        return 1
    elif n > 2:
        return naive_fibbonachi(n-1) + naive_fibbonachi(n-2)
    else:
        return -1


def fibbonachi_memoized(n, memo={}):
    """
    Вычисляет n-ое число Фибоначчи с мемоизацией.
    Аргументы:
        n: целое число — позиция числа Фибоначчи в последовательности.
        memo: словарь для хранения уже вычисленных значений Фибоначчи.
    Возвращает:
        n-ое число Фибоначчи
    """
    global fib_memo_calls
    fib_memo_calls += 1
    if n in memo:
        return memo[n]
    if n > 0 and n < 3:
        return 1
    elif n > 2:
        memo[n] = (fibbonachi_memoized(n-1, memo) +
                   fibbonachi_memoized(n-2, memo))
        return memo[n]
    else:
        return -1


def compare_fibbonachi(n):
    """
    Сравнивает результаты вычисления n-го числа Фибоначчи с мемоизацией и без.
    Аргументы:
        n: целое число — позиция числа Фибоначчи в последовательности.
    Возвращает:
        Словарь содержащий два ключа time, calls значениями
        которых являются кортежи из двух значений:
        (результат без мемоизации, результат с мемоизацией).
    """
    global fib_memo_calls
    global fib_calls

    start1 = timeit.default_timer()
    naive_fibbonachi(n)
    end1 = timeit.default_timer()
    fib_time = (end1 - start1) * 1000

    fib_count = fib_calls
    fib_calls = 0

    start2 = timeit.default_timer()
    fibbonachi_memoized(n)
    end2 = timeit.default_timer()
    fib_memo_time = (end2 - start2) * 1000

    fib_memo_count = fib_memo_calls
    fib_memo_calls = 0

    result = {"time": (fib_time, fib_memo_time),
              "calls": (fib_count, fib_memo_count)}

    return result


def Visualization(sizes):
    """
    Визуализация результатов замеров времени вычисления числа Фибоначчи
    с мемоизацией и без.
    """
    naive_times = []
    memoized_times = []
    print(sizes)
    for size in sizes:
        result = compare_fibbonachi(size)
        naive_times.append(result["time"][0])
        memoized_times.append(result["time"][1])

    plt.plot(sizes, naive_times, marker="o", color="red", label="Naive")
    plt.plot(sizes, memoized_times, marker="o", color="blue", label="Memoized")
    plt.xlabel("n (индекс числа Фибоначчи)")
    plt.ylabel("Время выполнения (ms)")
    plt.title("Сравнение времени вычисления "
              "числа Фибоначчи с мемоизацией и без")
    plt.legend(loc="upper left", title="Метод")
    plt.savefig("report/fibonacci_comparison.png", dpi=300, bbox_inches='tight')
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
    print(f"{naive_times} - naive \n {memoized_times} - memoized")
