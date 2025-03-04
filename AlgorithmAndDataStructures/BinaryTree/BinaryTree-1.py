class Node:
    def __init__(self, key):
        self.val = key
        self.count = 1  # Добавляем поле для подсчета повторений
        self.left = None
        self.right = None    

def insert(current, key):
    if current is None:
        return Node(key)
    if current.val == key:
        current.count += 1
    elif current.val < key:
        current.right = insert(current.right, key)
    else:
        current.left = insert(current.left, key)
    return current

def print_tree(current):
    if current:
        print_tree(current.left)
        print(f"{current.val}({current.count})", end=" ") 
        print_tree(current.right)

def find_left(current):
    if current is None:
        print("Дерево не имеет вершин")
        return None
    while current.left:
        current = current.left
    return current

def assign_left_leaf_value(current):
    left_leaf = find_left(current)
    if left_leaf is not None:
        return left_leaf.val
    return None

def count_occurrences(current, E):
    if current is None:
        return 0
    count = current.count if current.val == E else 0
    return count + count_occurrences(current.left, E) + count_occurrences(current.right, E)

def create_tree_from_input():
    root = None
    print("Введите значения для дерева. Для завершения ввода введите 'e'.")
    while True:
        user_input = input("Введите число: ")
        if user_input.lower() == "e":
            break
        try:
            values = list(map(int, user_input.split()))
            for value in values:
                root = insert(root, value)
        except ValueError:
            print("Неверный ввод, попробуйте снова.")
    return root


root = create_tree_from_input()

print("\nДерево (значение(количество повторений)):")
print_tree(root)
print("\n")

E = assign_left_leaf_value(root)
print("Значение самого левого листа:", E)

if E is not None:
    occurrences = count_occurrences(root, E)
    print(f"Число вхождений {E} в дереве: {occurrences}")