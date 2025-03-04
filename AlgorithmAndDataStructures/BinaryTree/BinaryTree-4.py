class Node:
    def __init__(self, key):
        self.val = float(key)
        self.left = None
        self.right = None    

def insert(current, key):
    if current is None:
        return Node(key)
    if key < current.val:
        current.left = insert(current.left, key)
    else:
        current.right = insert(current.right, key)
    return current

def print_tree(current):
    """Печатает дерево в порядке возрастания"""
    if current:
        print_tree(current.left)
        print(current.val, end=" ")
        print_tree(current.right)

def find_min(current):
    """Находит минимальное значение в дереве"""
    while current.left:
        current = current.left
    return current.val

def find_max(current):
    """Находит максимальное значение в дереве"""
    while current.right:
        current = current.right
    return current.val

def print_leaves(current):
    """Выводит значения всех листьев дерева"""
    if current:
        if not current.left and not current.right:
            print(current.val, end=" ")
        print_leaves(current.left)
        print_leaves(current.right)

# Ввод дерева
def create_tree_from_input():
    root = None
    print("Введите числа для дерева (вещественные). Для завершения введите 'end'.")
    while True:
        user_input = input("Введите число: ")
        if user_input.lower() == "end":
            break
        try:
            values = map(float, user_input.split())
            for value in values:
                root = insert(root, value)
        except ValueError:
            print("Ошибка ввода, попробуйте снова.")
    return root

root = create_tree_from_input()

if root:
    print("\nДерево:")
    print_tree(root)
    print("\n")

    print(f"Минимальное значение: {find_min(root)}")
    print(f"Максимальное значение: {find_max(root)}")

    print("\nЛистья дерева:")
    print_leaves(root)
    print("\n")
else:
    print("Дерево пустое.")