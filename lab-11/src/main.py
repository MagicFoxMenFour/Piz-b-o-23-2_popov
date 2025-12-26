# main.py

from modules.kmp_search import kmp_search, naive_search
from modules.prefix_function import prefix_function
from modules.z_function import z_function, find_substring_z
from modules.boier_mura import boier_mura
from modules.perfomance_analysis import Visualisation
from modules.string_matching import find_period, cyclic_shift

string = "acabababcababc"
pattern = "abcab"

print("String:", string)
print("Pattern:", pattern)

print("\nPrefix Function:", prefix_function(string))

print("kpm_search occurrences:", kmp_search(pattern, string))

print("naive_search occurrences:", naive_search(pattern, string))

print("Z-Function:", z_function(string))
print("find_substring_using_z_function occurrences:",
      find_substring_z(pattern, string))

print("boier_mura occurrences:", boier_mura(pattern, string))

# Performance Analysis Visualization
Sizes = [1000, 5000, 10000, 20000, 50000, 100000, 200000]
pat_sizes = [5, 10, 20, 50, 100, 200, 500]
Visualisation(Sizes, pat_sizes)

string_for_period = "abcabcabcabc"
period_length = find_period(string_for_period)
print(f"\nString for period finding: {string_for_period}")
print("prefix_function:", prefix_function(string_for_period))
print(f"Minimal period length: {period_length}")

a = "abcd"
b = "cdab"
print(f"\nIs '{b}' a cyclic shift of '{a}'? {cyclic_shift(a, b)}")


# Характеристики вычислительной машины
pc_info = """
Характеристики ПК для тестирования:
- Процессор: Intel Core i5-11500H @ 2.50GHz
- Оперативная память: 8 gb DDR4
- ОС: Windows 11
- Python: 3.12
"""
print(pc_info)
