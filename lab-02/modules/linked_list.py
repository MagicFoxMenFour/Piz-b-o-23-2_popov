class Node:
    """
    Класс узла односвязного списка.
    Аргументы:
        value: Значение, хранимое в узле.
        next: Ссылка на следующий узел (или None).
    """

    def __init__(self, value, next=None):
        """
        Инициализация узла.
        value: Значение узла.
        next: Следующий узел (Node) или None.
        """
        self.value = value
        self.next = next


class LinkedList:
    """
    Класс односвязного списка.
    Содержит методы для вставки, удаления и обхода элементов.
    """

    def __init__(self):
        """
        Инициализация пустого списка.
        head: Ссылка на первый элемент (начало списка).
        tail: Ссылка на последний элемент (конец списка).
        """
        self.head = None
        self.tail = None

    def insert_at_start(self, value):
        """
        Вставляет новый элемент в начало (head) односвязного списка.
        Если список пуст, новый элемент становится и head, и tail.
        Аргументы:
            value: Значение, которое будет храниться в новом узле.
        Время выполнения: O(1)
        """
        new_node = Node(value)
        if self.head is None:  
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, value):
        """
        Вставляет новый элемент в конец (tail) односвязного списка.
        Если список пуст, новый элемент становится и head, и tail.
        Аргументы:
            value: Значение, которое будет храниться в новом узле.
        Время выполнения: O(1)
        """
        new_node = Node(value)
        if self.head is None:  
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete_from_start(self):
        """
        Удаляет элемент из начала (head) односвязного списка.
        Если список пуст, возбуждается исключение.
        Время выполнения: O(1)
        """
        if self.head is None:
            raise Exception("LinkedList empty")
        self.head = self.head.next
        if self.head is None:  
            self.tail = None

    def traversal(self):
        """
        Обходит односвязный список с начала (head) до конца (tail)
        и выводит значения элементов.
        Если список пуст, выводит сообщение.
        Время выполнения: O(N)
        """
        if self.head is None:
            print("LinkedList empty")
            return

        current = self.head
        while current:
            print(current.value)
            current = current.next
