class StudentNode:
    def __init__(self, last_name, first_name, birth_year, grades, total_score):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_year = birth_year
        self.grades = grades
        self.total_score = total_score
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, student):
        if not self.head:
            self.head = student
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = student
            student.next = self.head

    def print_list(self):
        if not self.head:
            return
        current = self.head
        while True:
            self.print_student(current)
            current = current.next
            if current == self.head:
                break

    def print_student(self, student):
        print(f"{student.last_name} {student.first_name}, {student.birth_year}, Балл: {student.total_score}")

    def selection_sort_by_last_name(self):
        if not self.head or self.head.next == self.head:
            return
        start = self.head
        while True:
            min_node = start
            current = start.next
            while current != self.head:
                if current.last_name < min_node.last_name:
                    min_node = current
                current = current.next
            if min_node != start:
                self.swap_data(start, min_node)
            start = start.next
            if start == self.head:
                break

    def swap_data(self, a, b):
        a.last_name, b.last_name = b.last_name, a.last_name
        a.first_name, b.first_name = b.first_name, a.first_name
        a.birth_year, b.birth_year = b.birth_year, a.birth_year
        a.grades, b.grades = b.grades, a.grades
        a.total_score, b.total_score = b.total_score, a.total_score

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, student):
        if not self.head:
            self.head = student
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = student

    def print_list(self):
        current = self.head
        while current:
            self.print_student(current)
            current = current.next

    def print_student(self, student):
        print(f"{student.last_name} {student.first_name}, {student.birth_year}, Балл: {student.total_score}")

    def selection_sort_by_last_name_desc(self):
        if not self.head or not self.head.next:
            return
        start = self.head
        while start:
            max_node = start
            current = start.next
            while current:
                if current.last_name > max_node.last_name:
                    max_node = current
                current = current.next
            if max_node != start:
                self.swap_data(start, max_node)
            start = start.next

    def swap_data(self, a, b):
        a.last_name, b.last_name = b.last_name, a.last_name
        a.first_name, b.first_name = b.first_name, a.first_name
        a.birth_year, b.birth_year = b.birth_year, a.birth_year
        a.grades, b.grades = b.grades, a.grades
        a.total_score, b.total_score = b.total_score, a.total_score

class TreeNode:
    def __init__(self, student):
        self.student = student
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, student):
        if not self.root:
            self.root = TreeNode(student)
        else:
            self._insert(self.root, student)

    def _insert(self, node, student):
        if student.birth_year < node.student.birth_year:
            if node.left:
                self._insert(node.left, student)
            else:
                node.left = TreeNode(student)
        else:
            if node.right:
                self._insert(node.right, student)
            else:
                node.right = TreeNode(student)

    def to_list(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.student)
            self._inorder(node.right, result)

    def selection_sort_by_age_desc(self):
        students = self.to_list()
        n = len(students)
        for i in range(n):
            max_idx = i
            for j in range(i + 1, n):
                if students[j].birth_year < students[max_idx].birth_year:
                    max_idx = j
            if max_idx != i:
                students[i], students[max_idx] = students[max_idx], students[i]
        return students

    def print_sorted_by_age(self):
        sorted_students = self.selection_sort_by_age_desc()
        for s in sorted_students:
            print(f"{s.last_name} {s.first_name}, {s.birth_year}, Балл: {s.total_score}")

    def selection_sort_by_age_asc(self):
        students = self.to_list()
        n = len(students)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if students[j].birth_year > students[min_idx].birth_year:
                    min_idx = j
            if min_idx != i:
                students[i], students[min_idx] = students[min_idx], students[i]
        return students

    def print_sorted_by_age_asc(self):
        sorted_students = self.selection_sort_by_age_asc()
        for s in sorted_students:
            print(f"{s.last_name} {s.first_name}, {s.birth_year}, Балл: {s.total_score}")

class Graph:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def print_list(self):
        for student in self.students:
            print(f"{student.last_name} {student.first_name}, {student.birth_year}, Балл: {student.total_score}")

    def selection_sort_by_score_asc(self):
        n = len(self.students)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if self.students[j].total_score < self.students[min_idx].total_score:
                    min_idx = j
            if min_idx != i:
                self.students[i], self.students[min_idx] = self.students[min_idx], self.students[i]

    def print_sorted_by_score(self):
        self.selection_sort_by_score_asc()
        for student in self.students:
            print(f"{student.last_name} {student.first_name}, {student.birth_year}, Балл: {student.total_score}")

    def print_list(self):
        for student in self.students:
            print(f"{student.last_name} {student.first_name}, {student.birth_year}, Балл: {student.total_score}")

    def selection_sort_by_score_desc(self):
        n = len(self.students)
        for i in range(n):
            max_idx = i
            for j in range(i + 1, n):
                if self.students[j].total_score > self.students[max_idx].total_score:
                    max_idx = j
            if max_idx != i:
                self.students[i], self.students[max_idx] = self.students[max_idx], self.students[i]

    def print_sorted_by_score_desc(self):
        self.selection_sort_by_score_desc()
        for student in self.students:
            print(f"{student.last_name} {student.first_name}, {student.birth_year}, Балл: {student.total_score}")

class HashTable:
    def __init__(self):
        self.table = {}

    def add_student(self, student):
        self.table[student.last_name] = student

    def print_list(self):
        for student in self.table.values():
            print(f"{student.last_name} {student.first_name}, {student.birth_year}, Баллы: {student.total_score}, Экзамен 1: {student.exam_1_score}")

    def selection_sort_by_first_exam_asc(self):
        students = list(self.table.values())
        if not students:
            return []

        first_exam = list(students[0].grades.keys())[0]

        n = len(students)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if students[j].grades.get(first_exam, 0) < students[min_idx].grades.get(first_exam, 0):
                    min_idx = j
            if min_idx != i:
                students[i], students[min_idx] = students[min_idx], students[i]
        return students, first_exam

    def print_sorted_by_first_exam_asc(self):
        sorted_students, first_exam = self.selection_sort_by_first_exam_asc()
        for student in sorted_students:
            print(f"{student.last_name} {student.first_name}, {student.birth_year}, "
                f"Баллы: {student.total_score}, {first_exam}: {student.grades.get(first_exam, 0)}")
            
    def selection_sort_by_second_exam_desc(self):
        students = list(self.table.values())
        if not students or len(students[0].grades) < 2:
            return [], None

        second_exam = list(students[0].grades.keys())[1]

        n = len(students)
        for i in range(n):
            max_idx = i
            for j in range(i + 1, n):
                if students[j].grades.get(second_exam, 0) > students[max_idx].grades.get(second_exam, 0):
                    max_idx = j
            if max_idx != i:
                students[i], students[max_idx] = students[max_idx], students[i]
        return students, second_exam

    def print_sorted_by_second_exam_desc(self):
        sorted_students, second_exam = self.selection_sort_by_second_exam_desc()
        if second_exam is None:
            print("Недостаточно экзаменов для сортировки по второму.")
            return
        for student in sorted_students:
            print(f"{student.last_name} {student.first_name}, {student.birth_year}, "
                f"Баллы: {student.total_score}, {second_exam}: {student.grades.get(second_exam, 0)}")
    
    def selection_sort_by_third_exam_asc(self):
        students = list(self.table.values())
        if not students or len(students[0].grades) < 3:
            return [], None

        third_exam = list(students[0].grades.keys())[2]

        n = len(students)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if students[j].grades.get(third_exam, 0) < students[min_idx].grades.get(third_exam, 0):
                    min_idx = j
            if min_idx != i:
                students[i], students[min_idx] = students[min_idx], students[i]
        return students, third_exam

    def print_sorted_by_third_exam_asc(self):
        sorted_students, third_exam = self.selection_sort_by_third_exam_asc()
        if third_exam is None:
            print("Недостаточно экзаменов для сортировки по третьему.")
            return
        for student in sorted_students:
            print(f"{student.last_name} {student.first_name}, {student.birth_year}, "
                f"Баллы: {student.total_score}, {third_exam}: {student.grades.get(third_exam, 0)}")
    
    def selection_sort_by_fourth_exam_desc(self):
        students = list(self.table.values())
        if not students or len(students[0].grades) < 4:
            return [], None

        fourth_exam = list(students[0].grades.keys())[3]

        n = len(students)
        for i in range(n):
            max_idx = i
            for j in range(i + 1, n):
                if students[j].grades.get(fourth_exam, 0) > students[max_idx].grades.get(fourth_exam, 0):
                    max_idx = j
            if max_idx != i:
                students[i], students[max_idx] = students[max_idx], students[i]
        return students, fourth_exam

    def print_sorted_by_fourth_exam_desc(self):
        sorted_students, fourth_exam = self.selection_sort_by_fourth_exam_desc()
        if fourth_exam is None:
            print("Недостаточно экзаменов для сортировки по четвёртому.")
            return
        for student in sorted_students:
            print(f"{student.last_name} {student.first_name}, {student.birth_year}, "
                f"Баллы: {student.total_score}, {fourth_exam}: {student.grades.get(fourth_exam, 0)}")
            
students_data = [
    ("Иванов", "Иван", 2003, {"СиАД": 5, "Матеша": 4, "Физика": 5, "Прога": 4}, 18),
    ("Петров", "Алексей", 2002, {"СиАД": 4, "Матеша": 4, "Физика": 3, "Прога": 5}, 16),
    ("Сидоров", "Никита", 2004, {"СиАД": 5, "Матеша": 5, "Физика": 5, "Прога": 5}, 20),
    ("Алексеев", "Михаил", 2001, {"СиАД": 3, "Матеша": 4, "Физика": 4, "Прога": 4}, 15)
]

def main():
    while True:
        print("\nМеню сортировки:")
        print("1. Фамилии по алфавиту (кольцевой список)")
        print("2. Фамилии в обратном порядке (односвязный список)")
        print("3. По старшинству (от старшего) — бинарное дерево")
        print("4. По старшинству (от младшего) — бинарное дерево")
        print("5. По общему баллу (по возрастанию) — граф")
        print("6. По общему баллу (по убыванию) — граф")
        print("7. По результатам 1-го экзамена (по возрастанию) — хэш-таблица")
        print("8. По результатам 2-го экзамена (по убыванию) — хэш-таблица")
        print("9. По результатам 3-го экзамена (по возрастанию) — хэш-таблица")
        print("10. По результатам 4-го экзамена (по убыванию) — хэш-таблица")
        print("0. Выход")
        choice = input("Введите номер варианта: ")

        if choice == "1":
            group = CircularLinkedList()
            for data in students_data:
                group.append(StudentNode(*data))
            print("\nДо сортировки:")
            group.print_list()
            group.selection_sort_by_last_name()
            print("\nПосле сортировки (по алфавиту):")
            group.print_list()

        elif choice == "2":
            group = SinglyLinkedList()
            for data in students_data:
                group.append(StudentNode(*data))
            print("\nДо сортировки:")
            group.print_list()
            group.selection_sort_by_last_name_desc()
            print("\nПосле сортировки (в обратном алфавитном порядке):")
            group.print_list()

        elif choice == "3":
            tree = BinaryTree()
            for data in students_data:
                tree.insert(StudentNode(*data))
            print("\nСтуденты по старшинству (от старшего):")
            tree.print_sorted_by_age()

        elif choice == "4":
            tree = BinaryTree()
            for data in students_data:
                tree.insert(StudentNode(*data))
            print("\nСтуденты по старшинству (от младшего):")
            tree.print_sorted_by_age_asc()

        elif choice == "5":
            graph = Graph()
            for data in students_data:
                graph.add_student(StudentNode(*data))
            print("\nСтуденты по общему баллу (по возрастанию):")
            graph.print_sorted_by_score()

        elif choice == "6":
            graph = Graph()
            for data in students_data:
                graph.add_student(StudentNode(*data))
            print("\nСтуденты по общему баллу (по убыванию):")
            graph.print_sorted_by_score_desc()

        elif choice == "7":
            hash_table = HashTable()
            for data in students_data:
                hash_table.add_student(StudentNode(*data))

            print("\nСтуденты по результатам первого экзамена (по возрастанию):")
            hash_table.print_sorted_by_first_exam_asc()

        elif choice == "8":
            hash_table = HashTable()
            for data in students_data:
                hash_table.add_student(StudentNode(*data))

            print("\nСтуденты по результатам второго экзамена (по убыванию):")
            hash_table.print_sorted_by_second_exam_desc()

        elif choice == "9":
            hash_table = HashTable()
            for data in students_data:
                hash_table.add_student(StudentNode(*data))

            print("\nСтуденты по результатам третьего экзамена (по возрастанию):")
            hash_table.print_sorted_by_third_exam_asc()

        elif choice == "10":
            hash_table = HashTable()
            for data in students_data:
                hash_table.add_student(StudentNode(*data))

            print("\nСтуденты по результатам четвёртого экзамена (по убыванию):")
            hash_table.print_sorted_by_fourth_exam_desc()

        elif choice == "0":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

main()
