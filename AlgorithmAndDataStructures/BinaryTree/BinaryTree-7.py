class Node:
    def __init__(self, key):
        self.val = int(key)
        self.left = None
        self.right = None    

def insert(current, key):
    #Вставляет новый узел в дерево
    if current is None:
        return Node(key)
    if key < current.val:
        current.left = insert(current.left, key)
    elif key > current.val:
        current.right = insert(current.right, key)
    return current

def copy_tree(original):
    #Создает копию бинарного дерева
    if original is None:
        return None
    new_node = Node(original.val)
    new_node.left = copy_tree(original.left)
    new_node.right = copy_tree(original.right)
    return new_node

def print_tree(current):
    #Выводит дерево в порядке возрастания
    if current:
        print_tree(current.left)
        print(current.val, end=" ")
        print_tree(current.right)

def create_tree_from_input():
    root = None
    print("Введите целые числа для дерева. Для завершения введите 'e'.")
    while True:
        user_input = input("Введите число: ")
        if user_input.lower() == "e":
            break
        try:
            values = map(int, user_input.split())
            for value in values:
                root = insert(root, value)
        except ValueError:
            print("Ошибка ввода, попробуйте снова.")
    return root

root = create_tree_from_input()

if root:
    print("\nОригинальное дерево:")
    print_tree(root)
    print("\n")

    copied_root = copy_tree(root)

    print("\nКопия дерева:")
    print_tree(copied_root)
    print("\n")
else:
    print("Дерево пустое.")