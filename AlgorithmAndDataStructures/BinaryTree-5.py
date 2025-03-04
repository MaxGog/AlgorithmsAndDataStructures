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

def search_and_insert(current, key):
    """Определяет, есть ли ключ в дереве, и добавляет его, если нет"""
    if current is None:
        print(f"Элемент {key} не найден, добавляем в дерево.")
        return Node(key), True
    if key == current.val:
        print(f"Элемент {key} уже есть в дереве.")
        return current, False
    if key < current.val:
        current.left, added = search_and_insert(current.left, key)
    else:
        current.right, added = search_and_insert(current.right, key)
    return current, added

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

    key = int(input("\nВведите число для поиска или добавления: "))
    root, _ = search_and_insert(root, key)

    print("\nОбновленное дерево:")
    print_tree(root)
    print("\n")
else:
    print("Дерево пустое.")