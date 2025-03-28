class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.left = None
        self.right = None  

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def linear_search(self):
        result = []
        current = self.head
        while current:
            if current.data % 4 == 0:
                result.append(current.data)
            current = current.next
        return result

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = new_node
            new_node.next = self.head

    def linear_search(self):
        result = []
        current = self.head
        while current:
            if current.data % 4 == 0:
                result.append(current.data)
            current = current.next
            if current == self.head:
                break
        return result

    def print_list(self):
        current = self.head
        if current:
            while True:
                print(current.data, end=" -> ")
                current = current.next
                if current == self.head:
                    break
        print("... (circle)")


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left:
                self._insert(node.left, data)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self._insert(node.right, data)
            else:
                node.right = Node(data)

    def linear_search(self):
        result = []
        self._linear_search(self.root, result)
        return [data for data in result if data % 4 == 0]

    def _linear_search(self, node, result):
        if node:
            result.append(node.data)
            self._linear_search(node.left, result)
            self._linear_search(node.right, result)

    def print_tree(self):
        self._in_order_traversal(self.root)

    def _in_order_traversal(self, node):
        if node:
            self._in_order_traversal(node.left)
            print(node.data, end=" -> ")
            self._in_order_traversal(node.right)


if __name__ == "__main__":
    choice = input("Выберите структуру данных (1 - Односвязный список, 2 - Кольцевой список, 3 - Бинарное дерево): ")

    if choice == '1':
        ll = LinkedList()
        n = int(input("Введите количество элементов в списке: "))
        print("Введите элементы списка (через пробел):")
        elements = list(map(int, input().split()))
        for element in elements:
            ll.append(element)

        print("\nСписок:")
        ll.print_list()

        linear_result = ll.linear_search()
        print(f"Линейный поиск: элементы, кратные 4: {linear_result}")

        indexed_result = ll.indexed_search()
        print(f"Индексно-последовательный поиск: элементы, кратные 4: {indexed_result}")

    elif choice == '2':
        cll = CircularLinkedList()
        n = int(input("Введите количество элементов в списке: "))
        print("Введите элементы списка (через пробел):")
        elements = list(map(int, input().split()))
        for element in elements:
            cll.append(element)

        print("\nКольцевой список:")
        cll.print_list()

        linear_result = cll.linear_search()
        print(f"Линейный поиск: элементы, кратные 4: {linear_result}")

        indexed_result = cll.indexed_search()
        print(f"Индексно-последовательный поиск: элементы, кратные 4: {indexed_result}")

    elif choice == '3':
        bt = BinaryTree()
        n = int(input("Введите количество элементов в дереве: "))
        print("Введите элементы дерева (через пробел):")
        elements = list(map(int, input().split()))
        for element in elements:
            bt.insert(element)

        print("\nБинарное дерево:")
        bt.print_tree()

        linear_result = bt.linear_search()
        print(f"Линейный поиск: элементы, кратные 4: {linear_result}")

        indexed_result = bt.indexed_search()
        print(f"Индексно-последовательный поиск: элементы, кратные 4: {indexed_result}")

    else:
        print("Неверный выбор!")
