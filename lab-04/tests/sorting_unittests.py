import unittest
import src.modules.sorts as sorts
import src.modules.generate_data as gen_data


class SortingRandomDataTest(unittest.TestCase):
    def test_bubble_sort_random(self):
        data = gen_data.generate_random_data(1000)
        data_copy = data.copy()
        data.sort()
        self.assertEqual(sorts.bubble_sort(data_copy), data)

    def test_selection_sort_random(self):
        data = gen_data.generate_random_data(1000)
        data_copy = data.copy()
        data.sort()
        self.assertEqual(sorts.selection_sort(data_copy), data)

    def test_insertion_sort_random(self):
        data = gen_data.generate_random_data(1000)
        data_copy = data.copy()
        data.sort()
        self.assertEqual(sorts.insertion_sort(data_copy), data)

    def test_merge_sort_random(self):
        data = gen_data.generate_random_data(1000)
        data_copy = data.copy()
        data.sort()
        self.assertEqual(sorts.merge_sort(data_copy), data)

    def test_quick_sort_random(self):
        data = gen_data.generate_random_data(1000)
        data_copy = data.copy()
        data.sort()
        self.assertEqual(sorts.quick_sort(data_copy), data)


class SortingSortedDataTest(unittest.TestCase):
    def test_bubble_sort_sorted(self):
        data = gen_data.generate_sorted_data(1000)
        data_copy = data.copy()
        data.sort()
        self.assertEqual(sorts.bubble_sort(data_copy), data)

    def test_selection_sort_sorted(self):
        data = gen_data.generate_sorted_data(1000)
        data_copy = data.copy()
        data.sort()
        self.assertEqual(sorts.selection_sort(data_copy), data)

    def test_insertion_sort_sorted(self):
        data = gen_data.generate_sorted_data(1000)
        data_copy = data.copy()
        data.sort()
        self.assertEqual(sorts.insertion_sort(data_copy), data)

    def test_merge_sort_sorted(self):
        data = gen_data.generate_sorted_data(1000)
        data_copy = data.copy()
        data.sort()
        self.assertEqual(sorts.merge_sort(data_copy), data)

    def test_quick_sort_sorted(self):
        data = gen_data.generate_sorted_data(1000)
        data_copy = data.copy()
        data.sort()
        self.assertEqual(sorts.quick_sort(data_copy), data)


class SortingReversedDataTest(unittest.TestCase):
    def test_bubble_sort_reversed(self):
        data = gen_data.generate_reversed_data(1000)
        data_copy = data.copy()
        data.sort()
        self.assertEqual(sorts.bubble_sort(data_copy), data)

    def test_selection_sort_reversed(self):
        data = gen_data.generate_reversed_data(1000)
        data_copy = data.copy()
        data.sort()
        self.assertEqual(sorts.selection_sort(data_copy), data)

    def test_insertion_sort_reversed(self):
        data = gen_data.generate_reversed_data(1000)
        data_copy = data.copy()
        data.sort()
        self.assertEqual(sorts.insertion_sort(data_copy), data)

    def test_merge_sort_reversed(self):
        data = gen_data.generate_reversed_data(1000)
        data_copy = data.copy()
        data.sort()
        self.assertEqual(sorts.merge_sort(data_copy), data)

    def test_quick_sort_reversed(self):
        data = gen_data.generate_reversed_data(1000)
        data_copy = data.copy()
        data.sort()
        self.assertEqual(sorts.quick_sort(data_copy), data)


class SortingAlmostSortedDataTest(unittest.TestCase):
    def test_bubble_sort_almost_sorted(self):
        data = gen_data.generate_almost_sorted_data(1000)
        data_copy = data.copy()
        data.sort()
        self.assertEqual(sorts.bubble_sort(data_copy), data)

    def test_selection_sort_almost_sorted(self):
        data = gen_data.generate_almost_sorted_data(1000)
        data_copy = data.copy()
        data.sort()
        self.assertEqual(sorts.selection_sort(data_copy), data)

    def test_insertion_sort_almost_sorted(self):
        data = gen_data.generate_almost_sorted_data(1000)
        data_copy = data.copy()
        data.sort()
        self.assertEqual(sorts.insertion_sort(data_copy), data)

    def test_merge_sort_almost_sorted(self):
        data = gen_data.generate_almost_sorted_data(1000)
        data_copy = data.copy()
        data.sort()
        self.assertEqual(sorts.merge_sort(data_copy), data)

    def test_quick_sort_almost_sorted(self):
        data = gen_data.generate_almost_sorted_data(1000)
        data_copy = data.copy()
        data.sort()
        self.assertEqual(sorts.quick_sort(data_copy), data)
