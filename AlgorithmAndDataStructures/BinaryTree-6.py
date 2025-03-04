class Node:
    def __init__(self, key):
        self.val = int(key)
        self.left = None
        self.right = None    

def insert(current, key):
    """Вставляет новый узел в дерево"""
    if current is None:
        return Node(key)
    if key < current.val:
        current.left = insert(current.left, key)
    elif key > current.val:
        current.right = insert(current.right, key)
    return current

def find_path_length(current, key, depth=0):
    """Находит длину пути до элемента key (число ветвей).
       Если элемент не найден, возвращает -1.
    """
    if current is None:
        return -1
    if key == current.val:
        return depth
    elif key < current.val:
        return find_path_length(current.left, key, depth + 1)
    else:
        return find_path_length(current.right, key, depth + 1)

def find_max_depth(current):
    """Определяет максимальную глубину дерева (число ветвей в самом длинном пути)."""
    if current is None:
        return -1
    left_depth = find_max_depth(current.left)
    right_depth = find_max_depth(current.right)
    return max(left_depth, right_depth) + 1

def print_tree(current):
    """Выводит дерево в порядке возрастания"""
    if current:
        print_tree(current.left)
        print(current.val, end=" ")
        print_tree(current.right)

# Ввод дерева
def create_tree_from_input():
    root = None
    print("Введите целые числа для дерева. Для завершения введите 'end'.")
    while True:
        user_input = input("Введите число: ")
        if user_input.lower() == "end":
            break
        try:
            values = map(int, user_input.split())
            for value in values:
                root = insert(root, value)
        except ValueError:
            print("Ошибка ввода, попробуйте снова.")
    return root

# Основная программа
root = create_tree_from_input()

if root:
    print("\nДерево:")
    print_tree(root)
    print("\n")

    key = int(input("\nВведите число для поиска его пути от корня: "))
    path_length = find_path_length(root, key)
    if path_length != -1:
        print(f"Длина пути до {key}: {path_length}")
    else:
        print(f"Элемент {key} не найден в дереве.")

    max_depth = find_max_depth(root)
    print(f"Максимальная глубина дерева: {max_depth}")
else:
    print("Дерево пустое.")