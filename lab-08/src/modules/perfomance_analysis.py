# perfomance.analysis.py

import matplotlib.pyplot as plt
import timeit
from modules.greedy_algorithms import (
    huffman_coding, generate_frequencies, generate_text)


def measure_huffman_time(size, repeats=3):
    """
    Измеряет время выполнения алгоритма Хаффмана для текста заданного размера.
    Args:
        size: размер текста
        repeats: количество повторов для усреднения

    Returns:
        среднее время выполнения в миллисекундах
    """
    times = []
    for _ in range(repeats):
        text = generate_text(size)
        frequencies = generate_frequencies(text)
        start = timeit.default_timer()
        huffman_coding(frequencies)
        end = timeit.default_timer()
        times.append(end - start)
    return (sum(times) / repeats) * 1000  # в миллисекунда


def visualization(sizes):
    """
    Визуализация времени выполнения алгоритма Хаффмана
    Args:
        sizes: список размеров для тестирования
    """
    huffman_times = []
    for size in sizes:
        huffman_times.append(measure_huffman_time(size))
    print("Время выполнения алгоритма Хаффмана для разных размеров:")
    print(huffman_times)
    print("")
    plt.plot(sizes, huffman_times, marker='o', color="red", label="huffman")
    plt.xlabel("Количество элементов n")
    plt.ylabel("Время выполнения ms")
    plt.title("Время выполнения алгоритма Хаффмана")
    plt.legend(loc="upper left", title="Метод")
    plt.savefig("./report/Huffman.png", dpi=300, bbox_inches="tight")
    plt.show()
