class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(current_node.left, data)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(current_node.right, data)

    def linear_search_by_index_sum(self):
        return self._linear_search_by_index_sum(self.root, 0, 0)

    def _linear_search_by_index_sum(self, node, index_sum, comparisons):
        if not node:
            return None, comparisons
        comparisons += 1
        if node.data == index_sum:
            return node, comparisons
        left_result, left_comparisons = self._linear_search_by_index_sum(node.left, index_sum + 1, comparisons)
        if left_result:
            return left_result, left_comparisons
        return self._linear_search_by_index_sum(node.right, index_sum + 1, left_comparisons)

    def print_tree(self):
        if self.root:
            self._print_tree(self.root)
        print()

    def _print_tree(self, node):
        if node:
            self._print_tree(node.left)
            print(node.data, end=" ")
            self._print_tree(node.right)

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

    def linear_search_by_index_sum(self):
        current = self.head
        index_sum = 0
        comparisons = 0
        index = 0
        while current:
            index_sum += index
            comparisons += 1
            if current.data == index_sum:
                return current, comparisons
            current = current.next
            index += 1
        return None, comparisons

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

    def linear_search_by_index_sum(self):
        current = self.head
        index_sum = 0
        comparisons = 0
        index = 0
        if not current:
            return None, comparisons
        while True:
            index_sum += index
            comparisons += 1
            if current.data == index_sum:
                return current, comparisons
            current = current.next
            index += 1
            if current == self.head:
                break
        return None, comparisons

    def print_list(self):
        if not self.head:
            print("Empty List")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("... (circular)")

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
        tree = BinaryTree()
        for element in elements:
            tree.insert(element)
        structure = tree
        structure_type = "Бинарное дерево"
    elif choice == '2':
        sll = SinglyLinkedList()
        for element in elements:
            sll.append(element)
        structure = sll
        structure_type = "Односвязный список"
    elif choice == '3':
        cll = CircularLinkedList()
        for element in elements:
            cll.append(element)
        structure = cll
        structure_type = "Кольцевой список"
    else:
        print("Некорректный выбор.")

    print(f"Вы выбрали: {structure_type}")
    if choice == '1':
        print("Дерево элементов:")
        structure.print_tree()
    else:
        print("Список элементов:")
        structure.print_list()

    found_node, comparisons = structure.linear_search_by_index_sum()
    if found_node:
        print(f"Элемент {found_node.data} найден. Количество сравнений: {comparisons}.")
    else:
        print(f"Элемент не найден. Количество сравнений: {comparisons}.")
