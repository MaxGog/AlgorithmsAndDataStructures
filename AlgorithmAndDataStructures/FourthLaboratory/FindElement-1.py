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
        if not self.head:
            return None
        return self.head

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
        if not self.head:
            return None
        return self.head

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

    def find_min(self):
        current = self.root
        while current and current.left:
            current = current.left
        return current

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
        elements = list(map(int, input("Введите элементы списка (через пробел): ").split()))
        for element in elements:
            ll.append(element)

        print("\nСписок:")
        ll.print_list()
        min_node = ll.linear_search()
        if min_node:
            print(f"Линейный поиск: наименьший элемент = {min_node.data}")

    elif choice == '2':
        cll = CircularLinkedList()
        n = int(input("Введите количество элементов в списке: "))
        print("Введите элементы списка (через пробел):")
        elements = list(map(int, input().split()))
        for element in elements:
            cll.append(element)

        print("\nКольцевой список:")
        cll.print_list()

        min_node = cll.linear_search()
        if min_node:
            print(f"Линейный поиск: наименьший элемент = {min_node.data}")

    elif choice == '3':
        bt = BinaryTree()
        n = int(input("Введите количество элементов в дереве: "))
        print("Введите элементы дерева (через пробел):")
        elements = list(map(int, input().split()))
        for element in elements:
            bt.insert(element)

        print("\nБинарное дерево:")
        bt.print_tree()

        min_node = bt.find_min()
        if min_node:
            print(f"Наименьший элемент в бинарном дереве = {min_node.data}")
    else:
        print("Неверный выбор!")
