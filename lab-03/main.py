# main.py

from modules.recursion import factorial, fibbonachi, quick_power
from modules.memoization import compare_fibbonachi, Visualization
from modules.recursion_tasks import binary_search_recursive, print_directory_tree, hanoi

# Демонстрация работы функций из модуля recursion
print(factorial(1), factorial(5), factorial(7), factorial(9), factorial(-1))
print(fibbonachi(1), fibbonachi(5), fibbonachi(
    7), fibbonachi(15), fibbonachi(-1))
print(quick_power(5, 7), quick_power(2, 21), quick_power(2, 65))

# Демонстрация работы функций из модуля memoization
print(compare_fibbonachi(35))

# Демонстрация работы функций из модуля recursion_tasks
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(binary_search_recursive(arr, 7, 0, len(arr)-1))
print_directory_tree("./src")
hanoi(3, 'A', 'C', 'B')

# Демонстрация работы функции визуализации из модуля memoization
Visualization([5, 10, 15, 20, 25, 30, 35])
