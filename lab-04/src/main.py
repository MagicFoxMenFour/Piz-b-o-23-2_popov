# main.py

import modules.perfomance_test as perf_test

sizes = [100, 1000, 5000, 10000]
perf_test.Visualization(sizes)
perf_test.Create_summary_table(sizes)
