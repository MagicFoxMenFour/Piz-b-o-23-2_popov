# dynamic_programming.py

def fib_naive(n):
    """
    Вычисление n-го числа Фибоначчи с помощью наивной рекурсии.
    F(n) = F(n-1) + F(n-2)

    Args:
        n (int): Позиция числа Фибоначчи для вычисления.
    Returns:
        int: n-е число Фибоначчи.
    """
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

#   Временная сложность: O(2^n)
#   Пространственная сложность: O(n) (глубина рекурсии)


def fib_memo(n, memo=None):
    """
    Рекурсивное вычисление n-го числа Фибоначчи с мемоизацией (топ-даун).
    Args:
        n: Позиция числа Фибоначчи для вычисления.
        memo: Словарь для хранения уже вычисленных значений.
    Returns:
        int: n-е число Фибоначчи.
    """
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

#   Временная сложность: O(n)
#   Пространственная сложность: O(n) (для мемоизации и рекурсии)


def fib_tabulation(n):
    """
    Итеративное табличное решение (боттом-ап).
    Args:
        n: Позиция числа Фибоначчи для вычисления.
    Returns:
        int: n-е число Фибоначчи.
    """
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

#   Временная сложность: O(n)
#   Пространственная сложность: O(n) (для таблицы)


def knapsack_01(weights, values, capacity):
    """
    Вычисляет максимальную стоимость, которую можно унести
    в рюкзаке емкостью capacity с помощью
    динамического программирования (боттом-ап).
    Args:
        weights: список весов предметов
        values: список стоимостей предметов
        capacity: максимальная емкость рюкзака
    Returns:
        int: максимальная стоимость, которую можно унести
    """
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Заполнение таблицы
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]],
                               dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Временная сложность: O(n * capacity)
# Пространственная сложность: O(n * capacity)

def knapsack_01_with_items(weights, values, capacity):
    """
    Вычисляет максимальную стоимость и выбранные предметы, которые можно унести
    в рюкзаке емкостью capacity с
    помощью динамического программирования (боттом-ап).
    Args:
        weights: список весов предметов
        values: список стоимостей предметов
        capacity: максимальная емкость рюкзака
    Returns:
        tuple: (максимальная стоимость, список выбранных предметов)
    """
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Заполнение таблицы
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]],
                               dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Восстановление выбранных предметов
    w = capacity
    items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            items.append((values[i - 1], weights[i - 1]))  # индекс предмета
            w -= weights[i - 1]

    items.reverse()  # чтобы порядок соответствовал исходной последовательности
    return dp[n][capacity], items


def lcs(str1, str2):
    """
    Вычисляет длину наибольшей общей подпоследовательности (LCS)
    двух строк str1 и str2 с помощью динамического программирования (восходящий
    подход).
    Args:
        str1: первая строка
        str2: вторая строка
    Returns:
        int: длина LCS
    """
    n = len(str1)
    m = len(str2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Заполнение таблицы
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]

# Временная сложность: O(n * m)
# Пространственная сложность: O(n * m)


def lcs_with_sequence(str1, str2):
    """
    Вычисляет длину и саму наибольшую общую подпоследователь
    двух строк str1 и str2 с помощью динамического программирования (восходящий
    подход).
    Args:
        str1: первая строка
        str2: вторая строка
    Returns:
        tuple: (длина LCS, сама LCS)
    """
    n = len(str1)
    m = len(str2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Заполнение таблицы
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Восстановление самой LCS
    i, j = n, m
    sequence = []
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            sequence.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[n][m], ''.join(reversed(sequence))


def levenshtein_distance(str1, str2):
    """
    Вычисляет расстояние Левенштейна между двумя строками str1 и str2
    с помощью динамического программирования (восходящий подход).

    dp[i][j] — минимальное количество операций (вставка, удаление, замена),
    чтобы преобразовать первые i символов str1 в первые j символов str2.

    Args:
        str1: первая строка
        str2: вторая строка
    Returns:
        int: расстояние Левенштейна между str1 и str2
    """
    n = len(str1)
    m = len(str2)

    # Создаём таблицу (n+1) x (m+1)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Инициализация: преобразование пустой строки
    for i in range(n + 1):
        dp[i][0] = i  # i удалений
    for j in range(m + 1):
        dp[0][j] = j  # j вставок

    # Заполняем таблицу
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                cost = 0  # символы совпадают, замена не нужна
            else:
                cost = 1  # символы разные, потребуется замена

            dp[i][j] = min(
                dp[i - 1][j] + 1,      # удаление
                dp[i][j - 1] + 1,      # вставка
                dp[i - 1][j - 1] + cost  # замена
            )

    return dp[n][m]


# Временная сложность: O(n * m)
# Пространственная сложность: O(n * m)


def fib_tabulation_with_print(n):
    """
    Итеративное табличное решение (боттом-ап).
    Печатает таблицу вычислений на каждом шаге.
    Args:
        n: Позиция числа Фибоначчи для вычисления.
    Returns:
        int: n-е число Фибоначчи.
    """
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        print_fib_table(dp)
    return dp[n]


def print_fib_table(dp):
    """
    Печатает текущую таблицу вычислений Фибоначчи.

    Args:
        dp: список с вычисленными значениями Фибоначчи.
    """
    print("i:", end="  ")
    for i in range(len(dp)):
        print(i, end="  ")
    print("\nF(i):", end="  ")
    for val in dp:
        print(val, end="  ")
    print("\n")


def knapsack_1d(weights, values, capacity):
    """
    Оптимизированная версия 0/1 рюкзака.
    Используется один массив dp[w].

    dp[w] — максимальная стоимость при вместимости w.

    Время:  O(n * W)
    Память: O(W)
    """
    n = len(values)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):  # обратный проход
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

    return dp[capacity]
