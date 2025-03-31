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
        # Если значение уже существует, ничего не делаем
    
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, node, value):
        if node is None:
            return node
        
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Узел с одним или без детей
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Узел с двумя детьми: получаем минимальное значение в правом поддереве
            min_node = self._find_min(node.right)
            node.value = min_node.value
            node.right = self._delete_recursive(node.right, min_node.value)
        
        return node
    
    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def inorder_traversal(self):
        elements = []
        self._inorder_recursive(self.root, elements)
        return elements
    
    def _inorder_recursive(self, node, elements):
        if node is not None:
            self._inorder_recursive(node.left, elements)
            elements.append(node.value)
            self._inorder_recursive(node.right, elements)
    
    def find_and_process(self, condition, action="print", value=None, x=None, y=None):
        results = []
        self._find_and_process_recursive(self.root, condition, results, action, value, x, y)
        return results
    
    def _find_and_process_recursive(self, node, condition, results, action, value, x, y):
        if node is not None:
            self._find_and_process_recursive(node.left, condition, results, action, value, x, y)
            
            # Проверяем условие
            match condition:
                case "multiple":
                    if node.value % value == 0:
                        results.append(node.value)
                case "odd":
                    if node.value % 2 != 0:
                        results.append(node.value)
                case "greater":
                    if node.value > value:
                        results.append(node.value)
                case "less":
                    if node.value < value:
                        results.append(node.value)
                case "selected":
                    if node.value == value:
                        results.append(node.value)
                case "prime":
                    if self._is_prime(node.value):
                        results.append(node.value)
                case "composite":
                    if node.value > 1 and not self._is_prime(node.value):
                        results.append(node.value)
                case "interval":
                    if x <= node.value <= y:
                        results.append(node.value)
                case "digit_sum_greater":
                    if self._digit_sum(abs(node.value)) > value:
                        results.append(node.value)
                case "digit_sum_less":
                    if self._digit_sum(abs(node.value)) < value:
                        results.append(node.value)
                case "digit_sum_interval":
                    digit_sum = self._digit_sum(abs(node.value))
                    if x <= digit_sum <= y:
                        results.append(node.value)
                case "perfect_square":
                    sqrt_val = math.sqrt(abs(node.value))
                    if sqrt_val == int(sqrt_val):
                        results.append(node.value)
            
            self._find_and_process_recursive(node.right, condition, results, action, value, x, y)
    
    def _is_prime(self, n):
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
    
    def _digit_sum(self, n):
        return sum(int(digit) for digit in str(n))

def main():
    tree = BinaryTree()
    
    print("Выберите способ заполнения дерева:")
    print("1. Автоматическая генерация")
    print("2. Ручной ввод")
    choice = input("Ваш выбор (1/2): ")
    
    if choice == "1":
        # Автоматическая генерация 15 уникальных чисел
        elements = random.sample(range(-99, 100), 15)
        for elem in elements:
            tree.insert(elem)
        print("Сгенерированные элементы:", elements)
    elif choice == "2":
        # Ручной ввод 15 чисел
        print("Введите 15 уникальных чисел от -99 до 99:")
        for i in range(15):
            while True:
                try:
                    num = int(input(f"Число {i+1}: "))
                    if -99 <= num <= 99:
                        if not tree.search(num):
                            tree.insert(num)
                            break
                        else:
                            print("Это число уже есть в дереве. Введите другое.")
                    else:
                        print("Число должно быть в диапазоне от -99 до 99.")
                except ValueError:
                    print("Пожалуйста, введите целое число.")
    else:
        print("Неверный выбор. Используется автоматическая генерация.")
        elements = random.sample(range(-99, 100), 15)
        for elem in elements:
            tree.insert(elem)
        print("Сгенерированные элементы:", elements)
    
    print("\nТекущее дерево (inorder):", tree.inorder_traversal())
    
    # Меню для выбора условия
    print("\nВыберите условие для поиска/обработки:")
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
    
    condition_choice = input("Ваш выбор (1-12): ")
    
    condition_map = {
        "1": "multiple",
        "2": "odd",
        "3": "greater",
        "4": "less",
        "5": "selected",
        "6": "prime",
        "7": "composite",
        "8": "interval",
        "9": "digit_sum_greater",
        "10": "digit_sum_less",
        "11": "digit_sum_interval",
        "12": "perfect_square"
    }
    
    condition = condition_map.get(condition_choice)
    if not condition:
        print("Неверный выбор. Используется поиск простых чисел.")
        condition = "prime"
    
    value = None
    x = None
    y = None
    
    if condition in ["multiple", "greater", "less", "selected", "digit_sum_greater", "digit_sum_less"]:
        value = int(input(f"Введите значение N: "))
    elif condition in ["interval", "digit_sum_interval"]:
        x = int(input("Введите значение X: "))
        y = int(input("Введите значение Y: "))
    
    # Поиск элементов по условию
    results = tree.find_and_process(condition, "print", value, x, y)
    print(f"\nНайденные элементы ({condition}):", results)
    
    # Меню для действий с найденными элементами
    print("\nВыберите действие:")
    print("1. Удалить найденные элементы")
    print("2. Вставить новые элементы")
    print("3. Ничего не делать")
    
    action_choice = input("Ваш выбор (1-3): ")
    
    if action_choice == "1":
        # Удаление найденных элементов
        for num in results:
            tree.delete(num)
        print("Элементы удалены.")
        print("Обновленное дерево (inorder):", tree.inorder_traversal())
    elif action_choice == "2":
        # Вставка новых элементов
        print("Введите числа для вставки (разделяйте пробелом):")
        new_elements = input().split()
        for elem in new_elements:
            try:
                num = int(elem)
                if -99 <= num <= 99:
                    tree.insert(num)
                else:
                    print(f"Число {num} вне диапазона и не будет вставлено.")
            except ValueError:
                print(f"'{elem}' не является числом и будет пропущено.")
        print("Элементы вставлены.")
        print("Обновленное дерево (inorder):", tree.inorder_traversal())

if __name__ == "__main__":
    main()