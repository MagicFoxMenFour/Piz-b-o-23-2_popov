# main.py

import modules.perfomance_analysis as perf_test
from modules.hash_functions import simple_hash, polynomial_hash, djb2_hash
import modules.HistCollision as hist

perf_test.visualisation(size=100000)

hist.visualisation(simple_hash, func_name="Simple")
hist.visualisation(polynomial_hash, func_name="Polynomial")
hist.visualisation(djb2_hash, func_name="DJB2")

# Характеристики вычислительной машины
pc_info = """
Характеристики ПК для тестирования:
- Процессор: Intel Core i5-12500H @ 2.50GHz
- Оперативная память: 32 GB DDR4
- ОС: Windows 11
- Python: 3.12
"""
print(pc_info)
