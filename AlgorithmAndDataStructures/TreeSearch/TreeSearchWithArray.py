import random
import math

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class CircularList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.left = new_node
            new_node.right = new_node
        else:
            new_node.left = self.tail
            new_node.right = self.head
            self.tail.right = new_node
            self.head.left = new_node
            self.tail = new_node
        self.size += 1
    
    def display(self):
        if self.head is None:
            print("Кольцевой список пуст")
            return
        
        current = self.head
        print("Кольцевой список:", end=" ")
        for _ in range(self.size):
            print(current.value, end=" ")
            current = current.right
        print()

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
    
    def display(self):
        print("Бинарное дерево (in-order):", end=" ")
        self._display_recursive(self.root)
        print()
    
    def _display_recursive(self, node):
        if node is not None:
            self._display_recursive(node.left)
            print(node.value, end=" ")
            self._display_recursive(node.right)
    
    def search(self, condition_func):
        result = CircularList()
        self._search_recursive(self.root, condition_func, result)
        return result
    
    def _search_recursive(self, node, condition_func, result):
        if node is not None:
            self._search_recursive(node.left, condition_func, result)
            if condition_func(node.value):
                result.append(node.value)
            self._search_recursive(node.right, condition_func, result)
    
    def delete(self, condition_func):
        self.root = self._delete_recursive(self.root, condition_func)
    
    def _delete_recursive(self, node, condition_func):
        if node is None:
            return None
        
        node.left = self._delete_recursive(node.left, condition_func)
        node.right = self._delete_recursive(node.right, condition_func)
        
        if condition_func(node.value):
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_node = self._find_min(node.right)
                node.value = min_node.value
                node.right = self._delete_recursive(node.right, lambda x: x == min_node.value)
        return node
    
    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def sum_of_digits(n):
    n = abs(n)
    return sum(int(d) for d in str(n))

tree = BinaryTree()
choice = input("Хотите ввести элементы вручную? (y/n): ").lower()

if choice == 'y':
    print("Введите 15 чисел в диапазоне от -99 до 99:")
    for _ in range(15):
        while True:
            try:
                num = int(input())
                if -99 <= num <= 99:
                    tree.insert(num)
                    break
                else:
                    print("Число должно быть в диапазоне от -99 до 99. Попробуйте еще раз.")
            except ValueError:
                print("Некорректный ввод. Введите целое число.")
else:
    print("Генерация случайных чисел...")
    for _ in range(15):
        num = random.randint(-99, 99)
        tree.insert(num)

tree.display()

N = int(input("Введите число N: "))
X = int(input("Введите число X: "))
Y = int(input("Введите число Y: "))

conditions = [
    ("Числа кратные N", lambda x: x % N == 0),
    ("Нечетные числа", lambda x: x % 2 != 0),
    ("Числа > N", lambda x: x > N),
    ("Числа < N", lambda x: x < N),
    ("Числа по выбору (равные N)", lambda x: x == N),
    ("Простые числа", is_prime),
    ("Составные числа", lambda x: not is_prime(x) and x not in [-1, 0, 1]),
    ("Числа в интервале от X до Y", lambda x: X <= x <= Y),
    ("Числа, сумма цифр (по модулю) которого > N", lambda x: sum_of_digits(x) > N),
    ("Числа, сумма цифр (по модулю) которого < N", lambda x: sum_of_digits(x) < N),
    ("Числа, сумма цифр (по модулю) которого лежит в интервале от X до Y", lambda x: X <= sum_of_digits(x) <= Y),
    ("Числа, взятые по модулю, квадратный корень которых целое число", lambda x: math.sqrt(abs(x)) == int(math.sqrt(abs(x))))
]

while True:
    print("\nВыберите операцию:")
    for i, (name, _) in enumerate(conditions, 1):
        print(f"{i}. {name}")
    print("0. Выход")
    
    try:
        choice = int(input("Ваш выбор: "))
        if choice == 0:
            break
        if 1 <= choice <= len(conditions):
            name, condition = conditions[choice-1]
            
            print(f"\nПоиск: {name}")
            found = tree.search(condition)
            found.display()
            
            confirm = input(f"Удалить все элементы, удовлетворяющие условию '{name}'? (y/n): ").lower()
            if confirm == 'y':
                tree.delete(condition)
                print("Элементы удалены. Обновленное дерево:")
                tree.display()
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
    except ValueError:
        print("Некорректный ввод. Введите число.")
