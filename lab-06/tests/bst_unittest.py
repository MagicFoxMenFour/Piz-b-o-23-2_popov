import src.modules.binary_search_tree as bst
import src.modules.tree_traversal as trav
import unittest


class bstTest(unittest.TestCase):
    def setUp(self):
        self.tree = bst.BinarySearchTree()
        # создаём дерево с набором значений
        for v in [50, 30, 70, 20, 40, 60, 80]:
            self.tree.insert(v)

    def test_search_and_find_min_max(self):
        # проверка поиска
        node = self.tree.search(60)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 60)

        # find_min/find_max
        self.assertEqual(self.tree.find_min(self.tree.root).value, 20)
        self.assertEqual(self.tree.find_max(self.tree.root).value, 80)

    def test_is_valid_bst_and_height(self):
        self.assertTrue(self.tree.is_valid_bst())
        # высота: path 50->70->80 длина 3
        self.assertEqual(self.tree.height(self.tree.root), 3)

    def test_delete_leaf(self):
        self.assertTrue(self.tree.delete(20))
        self.assertIsNone(self.tree.search(20))
        self.assertTrue(self.tree.is_valid_bst())

    def test_delete_node_one_child(self):
        # вставим элемент, чтобы создать узел с одним ребёнком
        self.tree.insert(65)
        self.assertTrue(self.tree.delete(60))
        self.assertIsNone(self.tree.search(60))
        self.assertTrue(self.tree.is_valid_bst())

    def test_delete_node_two_children(self):
        # удалить узел 50 (корень) — у него два ребёнка
        self.assertTrue(self.tree.delete(50))
        self.assertIsNone(self.tree.search(50))
        self.assertTrue(self.tree.is_valid_bst())

    def test_traversals(self):
        result = []
        trav.inorder_recursive(self.tree.root, visit=result.append)
        self.assertEqual(result, [20, 30, 40, 50, 60, 70, 80])

        pre = []
        trav.preorder_recursive(self.tree.root, visit=pre.append)
        self.assertEqual(pre, [50, 30, 20, 40, 70, 60, 80])

        post = []
        trav.postorder_recursive(self.tree.root, visit=post.append)
        self.assertEqual(post, [20, 40, 30, 60, 80, 70, 50])

        it = []
        trav.inorder_iterative(self.tree.root, visit=it.append)
        self.assertEqual(it, [20, 30, 40, 50, 60, 70, 80])
