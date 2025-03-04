class Node:
    def __init__(self, key):
        self.val = float(key)  # Используем вещественные числа
        self.left = None
        self.right = None    

def insert(current, key):
    if current is None:
        return Node(key)
    if current.val == key:
        return current
    if current.val < key:
        current.right = insert(current.right, key)
    else:
        current.left = insert(current.left, key)
    return current

def print_tree(current):
    if current:
        print_tree(current.left)
        print(current.val, end=" ")
        print_tree(current.right)

def sum_and_count_nodes(current):
    """Возвращает кортеж (сумма всех значений, количество узлов)"""
    if current is None:
        return (0, 0)
    
    left_sum, left_count = sum_and_count_nodes(current.left)
    right_sum, right_count = sum_and_count_nodes(current.right)
    
    total_sum = left_sum + right_sum + current.val
    total_count = left_count + right_count + 1
    
    return (total_sum, total_count)

def compute_average(current):
    """Вычисляет среднее арифметическое значений в дереве"""
    total_sum, total_count = sum_and_count_nodes(current)
    if total_count == 0:
        return None
    return total_sum / total_count

def add_average_to_tree(current):
    """Добавляет в дерево вершину со значением среднего арифметического"""
    average = compute_average(current)
    if average is not None:
        return insert(current, average)
    return current  # Если дерево пустое, ничего не делаем

# Ввод дерева вручную
def create_tree_from_input():
    root = None
    print("Введите значения для дерева (вещественные числа). Для завершения ввода введите 'end'.")
    while True:
        user_input = input("Введите число: ")
        if user_input.lower() == "end":
            break
        try:
            values = list(map(float, user_input.split()))
            for value in values:
                root = insert(root, value)
        except ValueError:
            print("Неверный ввод, попробуйте снова.")
    return root

root = create_tree_from_input()

print("\nДерево:")
print_tree(root)
print("\n")

average_value = compute_average(root)
if average_value is not None:
    print(f"Среднее арифметическое всех вершин: {average_value:.4f}")
else:
    print("Дерево пустое, среднее арифметическое невозможно вычислить.")

root = add_average_to_tree(root)

print("\nДерево после добавления среднего арифметического:")
print_tree(root)
print("\n")