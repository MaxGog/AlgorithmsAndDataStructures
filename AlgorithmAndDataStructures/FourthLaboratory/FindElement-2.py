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
            if current.data > 30:
                result.append(current.data)
            current = current.next
        return result

    def binary_search(self):
        result = []
        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next
        
        low, high = 0, size - 1
        current = self.head
        found = False

        while low <= high:
            mid = (low + high) // 2
            for _ in range(mid):
                current = current.next
            if current.data > 30 and not found:
                found = True
                result.append(current.data)
            elif current.data > 30:
                result.append(current.data)
            if current.data <= 30:
                low = mid + 1
            else:
                high = mid - 1
            current = self.head
        return result

    def indexed_search(self):
        return self.linear_search()

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
            if current.data > 30:
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

    def find_min(self):
        current = self.root
        while current and current.left:
            current = current.left
        return current

    def linear_search(self):
        result = []
        self._linear_search(self.root, result)
        return [data for data in result if data > 30]

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
        print(f"Линейный поиск: элементы больше 30: {linear_result}")

        binary_result = ll.binary_search()
        print(f"Бинарный поиск: элементы больше 30: {binary_result}")

        indexed_result = ll.indexed_search()
        print(f"Индексно-последовательный поиск: элементы больше 30: {indexed_result}")

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
        print(f"Линейный поиск: элементы больше 30: {linear_result}")

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
        print(f"Линейный поиск: элементы больше 30: {linear_result}")

    else:
        print("Неверный выбор!")
