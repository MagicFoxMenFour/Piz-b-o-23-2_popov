# main.py

from modules.binary_search_tree import BinarySearchTree
from modules.analysis import run_experiment
import sys
from modules.perfomance_analysis import visualisation

# Tree visualize
tree = BinarySearchTree()


tree.insert(5)

tree.insert(3)
tree.insert(7)

tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)
tree.insert(1)


tree.visualize()


# analysis
sys.setrecursionlimit(40000)
sizes = [100, 1000, 5000, 10000]
res = run_experiment(
    sizes, trials_per_size=1000, repeats=3
)

# Perf_analysis
sizes = [100, 1000, 5000, 10000, 25000]
visualisation(sizes, out_png="./report/insert.png")


# Характеристики вычислительной машины
pc_info = """
Характеристики ПК для тестирования:
- Процессор: Intel Core i5-12500H @ 2.50GHz
- Оперативная память: 32 GB DDR4
- ОС: Windows 11
- Python: 3.12
"""
print(pc_info)
