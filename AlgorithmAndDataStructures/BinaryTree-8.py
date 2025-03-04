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

def equal_trees(t1, t2):
    """Проверяет, равны ли два дерева"""
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    return (t1.val == t2.val and  
            equal_trees(t1.left, t2.left) and  
            equal_trees(t1.right, t2.right))

def create_tree_from_input():
    """Создает дерево из пользовательского ввода"""
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

print("Создание первого дерева:")
tree1 = create_tree_from_input()

print("\nСоздание второго дерева:")
tree2 = create_tree_from_input()

if equal_trees(tree1, tree2):
    print("\nДеревья равны.")
else:
    print("\nДеревья не равны.")