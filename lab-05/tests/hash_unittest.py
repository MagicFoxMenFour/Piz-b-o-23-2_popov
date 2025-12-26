import unittest
import src.modules.hash_functions as hash_func
import src.modules.hash_table_chaining as HashTableC
import src.modules.hash_table_open_addressing as HashTableO


class HashFunctionTest(unittest.TestCase):
    def test_simple_hash(self):
        test = "abcd"
        self.assertEqual(hash_func.simple_hash(test), ord("a") * 4 + 1 + 2 + 3)

    def test_polynomial_hash(self):
        test = "abcd"
        self.assertEqual(hash_func.polynomial_hash(test), 5204554)

    def test_djb2_hash(self):
        test = "abc"
        self.assertEqual(hash_func.djb2_hash(test), 193485963)


class HashTableChainedTest(unittest.TestCase):
    def test_insert_get(self):
        test_data = ("apple", 23)
        table = HashTableC.Chaining_HashTable()
        table.insert(test_data[0], test_data[1])
        self.assertEqual(table.get("apple"), 23)

    def test_resize(self):
        table = HashTableC.Chaining_HashTable(initial_size=8)
        table.insert("a", 1)
        table.insert("ab", 1)
        table.insert("abc", 1)
        table.insert("abcd", 1)
        table.insert("abcde", 1)
        table.insert("abcdef", 1)
        table.insert("abcdefg", 1)
        self.assertEqual(table.size == 16, True)

    def test_shrink(self):
        table = HashTableC.Chaining_HashTable(initial_size=16)
        table.insert("a", 1)
        table.remove("a")
        self.assertEqual(table.size == 8, True)


class LinearHashTable(unittest.TestCase):
    def test_insert_get(self):
        test_data = ("apple", 23)
        table = HashTableO.Linear_HashTable()
        table.insert(test_data[0], test_data[1])
        self.assertEqual(table.get("apple"), 23)

    def test_remove(self):
        test_data = ("apple", 23)
        table = HashTableO.Linear_HashTable()
        table.insert(test_data[0], test_data[1])
        table.remove("apple")
        self.assertEqual(table.get("apple"), None)

    def test_resize(self):
        table = HashTableO.Linear_HashTable(size=8)
        table.insert("a", 1)
        table.insert("ab", 1)
        table.insert("abc", 1)
        table.insert("abcd", 1)
        table.insert("abcde", 1)
        table.insert("abcdef", 1)
        table.insert("abcdefg", 1)
        self.assertEqual(table.size == 16, True)


class DoubleHashTable(unittest.TestCase):
    def test_insert_get(self):
        test_data = ("apple", 23)
        table = HashTableO.DoubleHashingHashTable()
        table.insert(test_data[0], test_data[1])
        self.assertEqual(table.get("apple"), 23)

    def test_remove(self):
        test_data = ("apple", 23)
        table = HashTableO.DoubleHashingHashTable()
        table.insert(test_data[0], test_data[1])
        table.remove("apple")
        self.assertEqual(table.get("apple"), None)

    def test_resize(self):
        table = HashTableO.DoubleHashingHashTable(size=8)
        table.insert("a", 1)
        table.insert("ab", 1)
        table.insert("abc", 1)
        table.insert("abcd", 1)
        table.insert("abcde", 1)
        table.insert("abcdef", 1)
        table.insert("abcdefg", 1)
        self.assertEqual(table.size == 16, True)
