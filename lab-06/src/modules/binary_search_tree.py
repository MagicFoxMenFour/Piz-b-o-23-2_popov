# binary_search_tree.py

class TreeNode:
    """
    Класс отвечающий за реализацию узлов бинарного дерева.
    """

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    """
    Класс реализующий структуру данных бинарное дерево.
    Поддерживает визуализацию, проверку валидности и получение высоты
    """

    def __init__(self, root=None):
        self.root = root

    def insert(self, value):
        """
        Вставляет значение в дерево.

        Args:
            value: Значение для вставки в дерево
        """
        self.root = self._insert_rec(self.root, value)

    def _insert_rec(self, node, value):
        """
        Рекурсивно вставляет значение в дерево.

        Args:
            node: Текущий узел дерева
            value: Значение для вставки

        Returns:
            node: Обновленный узел дерева
        """
        if node is None:
            return TreeNode(value)
        if value == node.value:
            return node
        if value < node.value:
            node.left = self._insert_rec(node.left, value)
        else:
            node.right = self._insert_rec(node.right, value)
        return node

    # Среднее время: O(log n), Худшее время: O(n)

    def search(self, value):
        """
        Ищет значение в дереве, возвращает узел или None.

        Args:
            value: Искомое значение

        Returns:
            node: Найденный узел или None, если значение не найдено
        """
        return self._search_rec(self.root, value)

    def _search_rec(self, node, value):
        """
        Рекурсивный поиск значения в дереве.

        Args:
            node: Текущий узел дерева
            value: Искомое значение

        Returns:
            node: Найденный узел или None, если значение не найдено
        """
        if node is None:
            return None
        if value == node.value:
            return node
        if value < node.value:
            return self._search_rec(node.left, value)
        return self._search_rec(node.right, value)

    # Среднее время: O(log n), Худшее время: O(n)

    def delete(self, value):
        """
        Удаляет узел со значением value из дерева.
        Возвращает True, если удалено, иначе False.

        Args:
            value: Значение для удаления

        Returns:
            deleted: Флаг успешности удаления
        """
        self.root, deleted = self._delete_rec(self.root, value)
        return deleted

    # Среднее время: O(log n), Худшее время: O(n)

    def _delete_rec(self, node, value):
        """
        Рекурсивное удаление значения из дерева.

        Args:
            node: Текущий узел дерева
            value: Значение для удаления

        Returns:
            node: Обновленный узел дерева
            deleted: Флаг успешности удаления
        """
        if node is None:
            return node, False

        deleted = False
        if value < node.value:
            node.left, deleted = self._delete_rec(node.left, value)
        elif value > node.value:
            node.right, deleted = self._delete_rec(node.right, value)
        else:
            deleted = True
            # нет потомков
            if node.left is None and node.right is None:
                return None, True
            # один потомок
            if node.left is None:
                return node.right, True
            if node.right is None:
                return node.left, True
            # два потомка
            successor = self.find_min(node.right)
            node.value = successor.value
            node.right, _ = self._delete_rec(node.right, successor.value)

        return node, deleted

    def find_min(self, node):
        """
        Находит минимальный узел в поддереве node.

        Args:
            node: Корень поддерева

        Returns:
            node: Узел с минимальным значением
        """
        current = node
        if current is None:
            return None
        while current.left:
            current = current.left
        return current

    # Среднее время: O(log n), Худшее время: O(n)

    def find_max(self, node):
        """
        Находит максимальный узел в поддереве node.

        Args:
            node: Корень поддерева

        Returns:
            node: Узел с максимальным значением
        """
        current = node
        if current is None:
            return None
        while current.right:
            current = current.right
        return current

    # Среднее время: O(log n), Худшее время: O(n)

    def visualize(self, node=None, level=0):
        """
        Простая текстовая визуализация дерева (отступами).
        Печатает дерево повернутым: правые поддеревья сверху, левыe снизу.

        Args:
            node: Корень дерева/поддерева для визуализации
            level: Текущий уровень отступа
        """
        if node is None:
            node = self.root

        def _viz(n, lvl):
            if n is None:
                return
            _viz(n.right, lvl + 1)
            print("    " * lvl + str(n.value))
            _viz(n.left, lvl + 1)

        _viz(node, level)

    def is_valid_bst(self):
        """
        Проверяет, является ли дерево корректным BST.
        Временная сложность: O(n), Пространственная: O(h) рекурсивный стек.

        Returns:
            out: True если дерево является корректным BST, иначе False
        """
        def helper(node, low, high):
            if node is None:
                return True
            val = node.value
            if low is not None and val <= low:
                return False
            if high is not None and val >= high:
                return False
            left_ok = helper(node.left, low, val)
            if not left_ok:
                return False
            return helper(node.right, val, high)

        return helper(self.root, None, None)

    def height(self, node):
        """
        Вычисляет высоту дерева/поддерева (количество узлов в самом длинном
        пути от node до листа). Возвращает 0 для пустого поддерева.
        Временная сложность: O(n), Пространственная: O(h).

        Args:
            node: Корень дерева/поддерева

        Returns:
            height: Высота дерева/поддерева
        """
        if node is None:
            return 0
        left_h = self.height(node.left)
        right_h = self.height(node.right)
        return 1 + max(left_h, right_h)
