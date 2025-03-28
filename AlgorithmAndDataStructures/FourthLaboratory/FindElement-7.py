class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.comparisons = 0

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        self.comparisons += 1
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

    def linear_search(self, target):
        self.comparisons = 0
        result = self._in_order_traversal(self.root, [])
        for item in result:
            self.comparisons += 1
            if item == target:
                return True
        return False

    def _in_order_traversal(self, node, result):
        if node:
            self._in_order_traversal(node.left, result)
            result.append(node.data)
            self._in_order_traversal(node.right, result)
        return result

    def binary_search(self, target):
        self.comparisons = 0
        return self._binary_search_recursive(self.root, target)

    def _binary_search_recursive(self, node, target):
        if node is None:
            return False
        self.comparisons += 1
        if target < node.data:
            return self._binary_search_recursive(node.left, target)
        elif target > node.data:
            return self._binary_search_recursive(node.right, target)
        return True

    def indexed_search(self, target):
        self.comparisons = 0
        result = self._in_order_traversal(self.root, [])
        for i in range(len(result)):
            self.comparisons += 1
            if result[i] == target:
                return True
        return False

class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.comparisons = 0

    def append(self, data):
        new_node = SinglyLinkedListNode(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def linear_search(self, target):
        self.comparisons = 0
        current = self.head
        while current:
            self.comparisons += 1
            if current.data == target:
                return True
            current = current.next
        return False

    def indexed_search(self, target):
        self.comparisons = 0
        current = self.head
        index = 0
        while current:
            self.comparisons += 1
            if index == target:
                return current.data == target
            current = current.next
            index += 1
        return False

class CircularLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.comparisons = 0

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

    def linear_search(self, target):
        self.comparisons = 0
        if self.head:
            current = self.head
            while True:
                self.comparisons += 1
                if current.data == target:
                    return True
                current = current.next
                if current == self.head:
                    break
        return False

    def indexed_search(self, target):
        self.comparisons = 0
        current = self.head
        index = 0
        while current:
            self.comparisons += 1
            if index == target:
                return current.data == target
            current = current.next
            index += 1
            if current == self.head:
                break
        return False

if __name__ == "__main__":
    print("Выберите структуру данных:")
    print("1. Бинарное дерево")
    print("2. Односвязный список")
    print("3. Кольцевой список")
    choice = input("Введите номер (1/2/3): ")

    n = int(input("Введите количество элементов: "))
    print("Введите элементы (через пробел):")
    elements = list(map(int, input().split()))

    target = int(input("Введите элемент для поиска: "))

    if choice == '1':
        bst = BinaryTree()
        for element in elements:
            bst.insert(element)

        search_type = input("Выберите тип поиска (1 - Линейный, 2 - Бинарный, 3 - Индексно-последовательный): ")
        if search_type == '1':
            found = bst.linear_search(target)
        elif search_type == '2':
            found = bst.binary_search(target)
        elif search_type == '3':
            found = bst.indexed_search(target)
        else:
            print("Некорректный выбор поиска.")

        print(f"Элемент {'найден' if found else 'не найден'}. Количество сравнений: {bst.comparisons}")

    elif choice == '2':
        sll = SinglyLinkedList()
        for element in elements:
            sll.append(element)

        search_type = input("Выберите тип поиска (1 - Линейный, 3 - Индексно-последовательный): ")
        if search_type == '1':
            found = sll.linear_search(target)
        elif search_type == '3':
            found = sll.indexed_search(target)
        else:
            print("Некорректный выбор поиска.")

        print(f"Элемент {'найден' if found else 'не найден'}. Количество сравнений: {sll.comparisons}")

    elif choice == '3':
        cll = CircularLinkedList()
        for element in elements:
            cll.append(element)

        search_type = input("Выберите тип поиска (1 - Линейный, 3 - Индексно-последовательный): ")
        if search_type == '1':
            found = cll.linear_search(target)
        elif search_type == '3':
            found = cll.indexed_search(target)
        else:
            print("Некорректный выбор поиска.")

        print(f"Элемент {'найден' if found else 'не найден'}. Количество сравнений: {cll.comparisons}")

    else:
        print("Некорректный выбор. Программа завершена.")
