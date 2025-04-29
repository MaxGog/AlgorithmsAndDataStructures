from datetime import datetime, timedelta
from collections import defaultdict

class Node:
    def __init__(self, number, brand, owner, last_repair_date, due_date, repair_count):
        self.number = number
        self.brand = brand
        self.owner = owner
        self.last_repair_date = last_repair_date
        self.due_date = due_date
        self.repair_count = repair_count
        self.next = None


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.cars = []
        self.left = None
        self.right = None

class CarList:
    def __init__(self):
        self.head = None

    def add_car(self, car):
        if not self.head:
            self.head = car
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = car


    def sort_by_owner(self):
        if not self.head or not self.head.next:
            return

        sorted_head = None 

        current = self.head
        while current:
            next_node = current.next
            sorted_head = self._insert_sorted_by_owner(sorted_head, current)
            current = next_node

        self.head = sorted_head


    def _insert_sorted_by_owner(self, head, node_to_insert):
        if not head or node_to_insert.owner.lower() < head.owner.lower():
            node_to_insert.next = head
            return node_to_insert

        current = head
        while current.next and current.next.owner.lower() < node_to_insert.owner.lower():
            current = current.next

        node_to_insert.next = current.next
        current.next = node_to_insert

        return head

    def display(self):
        current = self.head
        while current:
            print_car_info(current)
            current = current.next

class CircularCarList:
    def __init__(self):
        self.head = None

    def add_car(self, car):
        if not self.head:
            self.head = car
            car.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = car
            car.next = self.head

    def sort_by_due_date(self):
        if not self.head or self.head.next == self.head:
            return

        cars = []
        current = self.head
        while True:
            cars.append(current)
            current = current.next
            if current == self.head:
                break

        cars.sort(key=lambda x: x.due_date)

        self.head = cars[0]
        for i in range(len(cars) - 1):
            cars[i].next = cars[i + 1]
        cars[-1].next = self.head

    def display(self):
        if not self.head:
            return
        current = self.head
        while True:
            print_car_info(current)
            current = current.next
            if current == self.head:
                break


class CarTree:
    def __init__(self):
        self.root = None

    def insert(self, car):
        if car.brand.lower() != "жигули":
            return
        self.root = self._insert_recursive(self.root, car)

    def _insert_recursive(self, node, car):
        if not node:
            new_node = TreeNode(car.repair_count)
            new_node.cars.append(car)
            return new_node
        if car.repair_count < node.key:
            node.left = self._insert_recursive(node.left, car)
        elif car.repair_count > node.key:
            node.right = self._insert_recursive(node.right, car)
        else:
            node.cars.append(car)
        return node

    def display_descending(self):
        self._reverse_inorder(self.root)

    def _reverse_inorder(self, node):
        if not node:
            return
        self._reverse_inorder(node.right)
        for car in node.cars:
            print(f'Ремонтов: {car.repair_count}')
            print_car_info(car)
        self._reverse_inorder(node.left)

class NumberTree:
    def __init__(self):
        self.root = None

    def insert(self, car):
        if car.repair_count != 2:
            return
        self.root = self._insert_recursive(self.root, car)

    def _insert_recursive(self, node, car):
        if not node:
            new_node = TreeNode(car.number)
            new_node.cars.append(car)
            return new_node
        if car.number > node.key:
            node.left = self._insert_recursive(node.left, car)
        elif car.number < node.key:
            node.right = self._insert_recursive(node.right, car)
        else:
            node.cars.append(car)
        return node

    def display_descending(self):
        self._reverse_inorder(self.root)

    def _reverse_inorder(self, node):
        if not node:
            return
        self._reverse_inorder(node.left)
        for car in node.cars:
            print_car_info(car)
        self._reverse_inorder(node.right)

class RepairGraph:
    def __init__(self):
        self.nodes = []

    def add_car(self, car):
        self.nodes.append(car)

    def display_sorted_by_due_date(self):
        sorted_cars = sorted(self.nodes, key=lambda car: car.due_date)
        for car in sorted_cars:
            print_car_info(car)

    def display_mercedes_owners_reverse(self):
        mercedes_owners = [car.owner for car in self.nodes if car.brand.lower() == "мерседес"]
        mercedes_owners.sort(reverse=True)
        for owner in mercedes_owners:
            print(owner)

    def display_brands_to_be_repaired_earlier(self):
        repair_cutoff_date = datetime.strptime("12.06.2024", "%d.%m.%Y").date()
        brands = {car.brand.lower() for car in self.nodes if car.due_date < repair_cutoff_date}
        sorted_brands = sorted(brands)
        for brand in sorted_brands:
            print(brand.capitalize())

class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return sum(ord(c) for c in key) % self.size

    def insert(self, car):
        index = self._hash(car.number)
        self.table[index].append(car)

    def get(self, brand):
        cars = []
        for bucket in self.table:
            for car in bucket:
                if car.brand.lower() == brand.lower():
                    cars.append(car)
        return cars

    def display_sorted(self, brand):
        cars = self.get(brand)
        cars.sort(key=lambda car: car.number)
        for car in cars:
            print_car_info(car)

    def get_cars_to_be_repaired_next_month(self):
        current_date = datetime.now().date()
        next_month = (current_date.replace(day=28) + timedelta(days=4)).replace(day=1)
        next_month_last_day = (next_month.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)

        cars_to_repair = []

        for bucket in self.table:
            for car in bucket:
                if next_month <= car.due_date <= next_month_last_day:
                    cars_to_repair.append(car)

        cars_to_repair.sort(key=lambda car: car.last_repair_date)

        return cars_to_repair

def print_car_info(car):
    print(f'Номер: {car.number}, Марка: {car.brand}, Владелец: {car.owner}')
    print(f'Последний ремонт: {car.last_repair_date.strftime("%d.%m.%Y")}')
    print(f'Срок ремонта до: {car.due_date.strftime("%d.%m.%Y")}')
    print(f'Количество предыдущих ремонтов: {car.repair_count}\n')

example_data = [
    ("А123ВС", "Toyota", "Иванов", "01.05.2024", "15.05.2024", 0),
    ("B456DE", "Honda", "Петров", "12.06.2024", "25.06.2024", 2),
    ("C789FG", "Жигули", "Алексеев", "10.04.2024", "20.04.2024", 5),
    ("D321GH", "Mazda", "Сидоров", "05.03.2024", "10.03.2024", 0),
    ("E654IJ", "Жигули", "Фёдоров", "12.02.2024", "22.02.2024", 3),
    ("F789KL", "Жигули", "Козлов", "02.01.2024", "10.01.2024", 5),
    ("M111MM", "Жигули", "Миронов", "01.02.2024", "10.02.2024", 2),
    ("X777XX", "BMW", "Новиков", "01.01.2024", "05.01.2024", 0),
    ("G555GG", "Мерседес", "Климова", "15.03.2024", "25.03.2024", 1),
    ("H888HH", "Мерседес", "Захаров", "20.03.2024", "30.03.2024", 2)
]

linear_list = CarList()
circular_list = CircularCarList()
car_tree = CarTree()
number_tree = NumberTree()
repair_graph = RepairGraph()

for number, brand, owner, last_str, due_str, repairs in example_data:
    last_date = datetime.strptime(last_str, "%d.%m.%Y").date()
    due_date = datetime.strptime(due_str, "%d.%m.%Y").date()
    car = Node(number, brand, owner, last_date, due_date, repairs)
    linear_list.add_car(car)
    circular_list.add_car(Node(number, brand, owner, last_date, due_date, repairs))
    car_tree.insert(Node(number, brand, owner, last_date, due_date, repairs))
    number_tree.insert(Node(number, brand, owner, last_date, due_date, repairs))
    repair_graph.add_car(Node(number, brand, owner, last_date, due_date, repairs))

class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return sum(ord(c) for c in key) % self.size

    def insert(self, car):
        index = self._hash(car.number)
        self.table[index].append(car)

    def get(self, brand):
        cars = []
        for bucket in self.table:
            for car in bucket:
                if car.brand.lower() == brand.lower():
                    cars.append(car)
        return cars

    def display_sorted(self, brand):
        cars = self.get(brand)
        cars.sort(key=lambda car: car.number)
        for car in cars:
            print_car_info(car)

    def get_owners_without_repair_since_last_year(self):
        current_date = datetime.now().date()
        last_year = current_date.replace(year=current_date.year - 1)
        owners = set()

        for bucket in self.table:
            for car in bucket:
                if car.last_repair_date < last_year:
                    owners.add(car.owner)

        return sorted(owners)

    def get_cars_to_be_repaired_next_month(self):
        current_date = datetime.now().date()
        
        next_month = current_date.replace(day=28) + timedelta(days=4)
        next_month_first_day = next_month.replace(day=1)
        
        next_month_last_day = (next_month_first_day.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)

        print(f"Следующий месяц: с {next_month_first_day} по {next_month_last_day}")

        cars_to_repair = []

        for bucket in self.table:
            for car in bucket:
                if next_month_first_day <= car.due_date <= next_month_last_day:
                    cars_to_repair.append(car)

        cars_to_repair.sort(key=lambda car: car.last_repair_date)

        return cars_to_repair

def menu():
    hash_table = HashTable()

    for number, brand, owner, last_str, due_str, repairs in example_data:
        last_date = datetime.strptime(last_str, "%d.%m.%Y").date()
        due_date = datetime.strptime(due_str, "%d.%m.%Y").date()
        car = Node(number, brand, owner, last_date, due_date, repairs)
        hash_table.insert(car)

    while True:
        print("\nМЕНЮ:")
        print("1. Сортировка по имени владельца (односвязный список)")
        print("2. Порядок ремонта по сроку (кольцевой список)")
        print("3. Жигули по убыванию количества ремонтов (бинарное дерево)")
        print("4. Машины с 2 ремонтами по убыванию номера (бинарное дерево)")
        print("5. Машины с 0 ремонтами по возрастанию даты окончания ремонта (граф)")
        print("6. Владельцы машин марки 'Мерседес' по алфавиту в обратном порядке (граф)")
        print("7. Марки машин, которые должны быть отремонтированы раньше всех (граф)")
        print("8. Вывести по возрастанию номера машин марки 'Жигули' (хэш-таблица)")
        print("9. Вывести имена владельцев, чьи машины не ремонтировались с прошлого года (хэш-таблица)")
        print("10. Вывести машины, которые надо отремонтировать к следующему месяцу по возрастанию даты последнего ремонта (хэш-таблица)")
        print("0. Выход")
        choice = input("Выберите пункт меню: ")

        if choice == '1':
            print("\n[1] Сортировка по имени владельца:\n")
            linear_list.sort_by_owner()
            linear_list.display()

        elif choice == '2':
            print("\n[2] Порядок ремонта по сроку:\n")
            circular_list.sort_by_due_date()
            circular_list.display()

        elif choice == '3':
            print("\n[3] Жигули по убыванию количества ремонтов:\n")
            car_tree.display_descending()

        elif choice == '4':
            print("\n[4] Машины с 2 ремонтами по убыванию номера:\n")
            number_tree.display_descending()

        elif choice == '5':
            print("\n[5] Машины с 0 ремонтами по возрастанию даты окончания ремонта:\n")
            repair_graph.display_sorted_by_due_date()

        elif choice == '6':
            print("\n[6] Владельцы машин марки 'Мерседес' по алфавиту в обратном порядке:\n")
            repair_graph.display_mercedes_owners_reverse()

        elif choice == '7':
            print("\n[7] Марки машин, которые должны быть отремонтированы раньше всех:\n")
            repair_graph.display_brands_to_be_repaired_earlier()

        elif choice == '8':
            print("\n[8] Вывод по возрастанию номеров машин марки 'Жигули':\n")
            hash_table.display_sorted("Жигули")

        elif choice == '9':
            print("\n[9] Вывод имён владельцев, чьи машины не ремонтировались с прошлого года:\n")
            owners = hash_table.get_owners_without_repair_since_last_year()
            for owner in owners:
                print(owner)

        elif choice == '10':
            print("\n[10] Вывод машин, которые надо отремонтировать к следующему месяцу по возрастанию даты последнего ремонта:\n")
            cars_to_repair = hash_table.get_cars_to_be_repaired_next_month()
            if not cars_to_repair:
                print("Нет машин, которые нужно отремонтировать в следующем месяце.")
            for car in cars_to_repair:
                print_car_info(car)

        elif choice == '0':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

menu()
