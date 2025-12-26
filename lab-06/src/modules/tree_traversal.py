# tree_traversal.py


def inorder_recursive(node, visit=print):
    """
    Рекурсивный in-order обход: left, root, right.
    Временная сложность: O(n), Пространственная: O(h) стек рекурсии.

    Args:
        node: Корень дерева/поддерева для обхода
        visit: Функция, применяемая к значению каждого узла
    """
    if node is None:
        return
    inorder_recursive(node.left, visit)
    visit(node.value)
    inorder_recursive(node.right, visit)


def preorder_recursive(node, visit=print):
    """
    Рекурсивный pre-order обход: root, left, right.
    Временная сложность: O(n), Пространственная: O(h) стек рекурсии.

    Args:
        node: Корень дерева/поддерева для обхода
        visit: Функция, применяемая к значению каждого узла
    """
    if node is None:
        return
    visit(node.value)
    preorder_recursive(node.left, visit)
    preorder_recursive(node.right, visit)


def postorder_recursive(node, visit=print):
    """
    Рекурсивный post-order обход: left, right, root.
    Временная сложность: O(n), Пространственная: O(h) стек рекурсии.

    Args:
        node: Корень дерева/поддерева для обхода
        visit: Функция, применяемая к значению каждого узла
    """
    if node is None:
        return
    postorder_recursive(node.left, visit)
    postorder_recursive(node.right, visit)
    visit(node.value)


def inorder_iterative(node, visit=print):
    """
    Итеративный in-order обход с использованием явного стека.
    Временная сложность: O(n), Пространственная: O(h) для стека.

    Args:
        node: Корень дерева/поддерева для обхода
        visit: Функция, применяемая к значению каждого узла
    """
    stack = []
    current = node
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        visit(current.value)
        current = current.right
