class Node:
    def __init__(self, key):
        self.val = float(key)
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

def extract_negative_nodes(current, new_tree=None):
    #Создает новое дерево из отрицательных значений
    if current is None:
        return new_tree

    if current.val < 0:
        new_tree = insert(new_tree, current.val)

    new_tree = extract_negative_nodes(current.left, new_tree)
    new_tree = extract_negative_nodes(current.right, new_tree)
    
    return new_tree

def create_tree_from_input():
    root = None
    print("Введите значения для дерева (вещественные числа). Для завершения ввода введите 'e'.")
    while True:
        user_input = input("Введите число: ")
        if user_input.lower() == "e":
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


negative_tree = extract_negative_nodes(root)

print("\nДерево из отрицательных чисел:")
print_tree(negative_tree)
print("\n")