class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)

    def linear_search(self):
        result = []
        self._in_order_traversal(self.root, result)
        return [x for x in result if x > 50]

    def _in_order_traversal(self, node, result):
        if node:
            self._in_order_traversal(node.left, result)
            result.append(node.data)
            self._in_order_traversal(node.right, result)

    def print_tree(self):
        result = []
        self._in_order_traversal(self.root, result)
        print(" -> ".join(map(str, result)))


class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = SinglyLinkedListNode(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def search_greater_than_50(self):
        result = []
        current = self.head
        while current:
            if current.data > 50:
                result.append(current.data)
            current = current.next
        return result

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

class CircularLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = CircularLinkedListNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        last = self.head
        while last.next != self.head:
            last = last.next
        last.next = new_node
        new_node.next = self.head

    def search_greater_than_50(self):
        result = []
        if self.head:
            current = self.head
            while True:
                if current.data > 50:
                    result.append(current.data)
                current = current.next
                if current == self.head:
                    break
        return result

    def print_list(self):
        if self.head:
            current = self.head
            while True:
                print(current.data, end=" -> ")
                current = current.next
                if current == self.head:
                    break
            print(f"(head: {self.head.data})")


if __name__ == "__main__":
    print("Выберите структуру данных:")
    print("1. Бинарное дерево")
    print("2. Односвязный список")
    print("3. Кольцевой список")
    choice = input("Введите номер (1/2/3): ")

    n = int(input("Введите количество элементов: "))
    print("Введите элементы (через пробел):")
    elements = list(map(int, input().split()))

    if choice == '1':
        bst = BinaryTree()
        for element in elements:
            bst.insert(element)
        print("\nДерево в симметричном порядке:")
        bst.print_tree()

        linear_result = bst.linear_search()
        print(f"Линейный поиск: числа, больше 50: {linear_result}")

    elif choice == '2':
        sll = SinglyLinkedList()
        for element in elements:
            sll.append(element)
        print("\nОдносвязный список:")
        sll.print_list()

        sll_result = sll.search_greater_than_50()
        print(f"Линейный поиск: числа, больше 50: {sll_result}")

    elif choice == '3':
        cll = CircularLinkedList()
        for element in elements:
            cll.append(element)

        print("\nКольцевой список:")
        cll.print_list()

        cll_result = cll.search_greater_than_50()
        print(f"Линейный поиск: числа, больше 50: {cll_result}")

    else:
        print("Некорректный выбор. Программа завершена.")
