# tasks.py

def coin_change(coins, amount):
    """
    Решение задачи размена монет с помощью
    динамического программирования (bottom-up).

    Args:
        coins: список доступных номиналов монет
        amount: сумма, которую нужно разменять
    Returns:
        int: минимальное количество монет, необходимое для размена суммы amount


    """
    # Инициализация dp: dp[i] = минимальное количество монет для суммы i
    # Используем значение amount+1 как "бесконечность"
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0  # 0 монет для суммы 0

    # Заполнение таблицы
    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a:
                dp[a] = min(dp[a], dp[a - coin] + 1)

    return dp[amount] if dp[amount] <= amount else -1


def lis(sequence):
    """
    Наибольшая возрастающая подпоследовательность (LIS) с DP.

    Args:
        sequence: входная последовательность чисел

    Returns:
        tuple: (длина LIS, сама LIS)
    """
    n = len(sequence)
    if n == 0:
        return 0, []

    # dp[i] — длина LIS, заканчивающейся на элементе i
    dp = [1] * n
    # prev[i] — индекс предыдущего элемента в LIS для восстановления
    prev = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if sequence[j] < sequence[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    # Находим индекс конца максимальной LIS
    max_len = max(dp)
    index = dp.index(max_len)

    # Восстанавливаем саму последовательность
    lis_seq = []
    while index != -1:
        lis_seq.append(sequence[index])
        index = prev[index]

    lis_seq.reverse()  # переворачиваем, чтобы получить правильный порядок

    return max_len, lis_seq
