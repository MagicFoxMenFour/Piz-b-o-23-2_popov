# main.py

from modules.heap import Heap
from modules.perfomance_analysis import visualization_build
from modules.perfomance_analysis import visualization_sort
from modules.perfomance_analysis import visualization_operations


sizes_build = [1000, 5000, 10000, 25000,
               100000, 250000, 500000, 1000000]
sizes_sort = [1000, 5000, 10000, 25000, 100000]
operation_sizes = [1000, 5000, 10000, 25000, 100000, 1000000]

visualization_build(sizes_build)
visualization_sort(sizes_sort)
visualization_operations(operation_sizes)

# Характеристики вычислительной машины
pc_info = """
Характеристики ПК для тестирования:
- Процессор: Intel Core i5-12500H @ 2.50GHz
- Оперативная память: 32 GB DDR4
- ОС: Windows 11
- Python: 3.12
"""
print(pc_info)


heap = Heap(True)
heap.build_heap([5, 2, 9, 1, 7, 6, 3])
heap.visualize()
