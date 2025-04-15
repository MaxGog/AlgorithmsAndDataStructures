import random
import math

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.value)
            self._inorder_traversal(node.right, result)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

def menu():
    tree = BinaryTree()
    
    choice = input("Выберите способ ввода (1 - случайные числа, 2 - вручную): ")
    
    if choice == '1':
        numbers = [random.randint(-99, 99) for _ in range(15)]
    elif choice == '2':
        numbers = []
        while len(numbers) < 15:
            try:
                num = int(input(f"Введите число {len(numbers) + 1} (от -99 до 99): "))
                if -99 <= num <= 99:
                    numbers.append(num)
                else:
                    print("Число вне диапазона!")
            except ValueError:
                print("Введите корректное число!")
    else:
        print("Неверный выбор! Выход из программы.")
        return
    
    print("Числа в дереве:", numbers)
    
    for num in numbers:
        tree.insert(num)

    while True:
        print("\nМеню:")
        print("1. Числа кратные N")
        print("2. Нечетные числа")
        print("3. Числа > N")
        print("4. Числа < N")
        print("5. Числа по выбору")
        print("6. Простые числа")
        print("7. Составные числа")
        print("8. Числа в интервале от X до Y")
        print("9. Числа, сумма цифр (по модулю) которого > N")
        print("10. Числа, сумма цифр (по модулю) которого < N")
        print("11. Числа, сумма цифр (по модулю) которого лежит в интервале от X до Y")
        print("12. Числа, взятые по модулю, квадратный корень которых целое число")
        print("0. Выход")

        choice = int(input("Выберите вариант: "))

        if choice == 0:
            break
        elif choice == 1:
            N = int(input("Введите N: "))
            result = [num for num in tree.inorder_traversal() if num % N == 0]
        elif choice == 2:
            result = [num for num in tree.inorder_traversal() if num % 2 != 0]
        elif choice == 3:
            N = int(input("Введите N: "))
            result = [num for num in tree.inorder_traversal() if num > N]
        elif choice == 4:
            N = int(input("Введите N: "))
            result = [num for num in tree.inorder_traversal() if num < N]
        elif choice == 5:
            selected = int(input("Введите число для поиска: "))
            result = [selected] if selected in tree.inorder_traversal() else []
        elif choice == 6:
            result = [num for num in tree.inorder_traversal() if is_prime(num)]
        elif choice == 7:
            result = [num for num in tree.inorder_traversal() if num > 1 and not is_prime(num)]
        elif choice == 8:
            X = int(input("Введите X: "))
            Y = int(input("Введите Y: "))
            result = [num for num in tree.inorder_traversal() if X <= num <= Y]
        elif choice == 9:
            N = int(input("Введите N: "))
            result = [num for num in tree.inorder_traversal() if sum_of_digits(num) > N]
        elif choice == 10:
            N = int(input("Введите N: "))
            result = [num for num in tree.inorder_traversal() if sum_of_digits(num) < N]
        elif choice == 11:
            X = int(input("Введите X: "))
            Y = int(input("Введите Y: "))
            result = [num for num in tree.inorder_traversal() if X <= sum_of_digits(num) <= Y]
        elif choice == 12:
            result = [num for num in tree.inorder_traversal() if math.sqrt(abs(num)).is_integer()]
        else:
            print("Неверный выбор, попробуйте снова.")
            continue

        print("Результат:", result)

if __name__ == "__main__":
    menu()