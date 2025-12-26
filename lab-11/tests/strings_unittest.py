# strings_unittest.py

import unittest
from src.modules.prefix_function import prefix_function
from src.modules.kmp_search import kmp_search, naive_search
from src.modules.z_function import z_function, find_substring_z
from src.modules.boier_mura import boier_mura


class TestStringAlgorithms(unittest.TestCase):
    def test_prefix_function(self):
        self.assertEqual(prefix_function("ababc"), [0, 0, 1, 2, 0])
        self.assertEqual(prefix_function("aaaa"), [0, 1, 2, 3])
        self.assertEqual(prefix_function("abcd"), [0, 0, 0, 0])

    def test_kmp_search(self):
        self.assertEqual(kmp_search("abc", "ababcabc"), [2, 5])
        self.assertEqual(kmp_search("a", "aaaaa"), [0, 1, 2, 3, 4])
        self.assertEqual(kmp_search("xyz", "abcdef"), [])

    def test_naive_search(self):
        self.assertEqual(naive_search("abc", "ababcabc"), [2, 5])
        self.assertEqual(naive_search("a", "aaaaa"), [0, 1, 2, 3, 4])
        self.assertEqual(naive_search("xyz", "abcdef"), [])

    def test_z_function(self):
        self.assertEqual(z_function("ababc"), [0, 0, 2, 0, 0])
        self.assertEqual(z_function("aaaa"), [0, 3, 2, 1])
        self.assertEqual(z_function("abcd"), [0, 0, 0, 0])

    def test_find_substring_z(self):
        self.assertEqual(find_substring_z("abc", "ababcabc"), [2, 5])
        self.assertEqual(find_substring_z("a", "aaaaa"), [0, 1, 2, 3, 4])
        self.assertEqual(find_substring_z("xyz", "abcdef"), [])

    def test_boier_mura(self):
        self.assertEqual(boier_mura("abc", "ababcabc"), [2, 5])
        self.assertEqual(boier_mura("a", "aaaaa"), [0, 1, 2, 3, 4])
        self.assertEqual(boier_mura("xyz", "abcdef"), [])
