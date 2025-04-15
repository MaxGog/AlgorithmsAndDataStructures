class Student:
    def __init__(self, last_name, first_name, birth_year, grades, total_score):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_year = birth_year
        self.grades = grades
        self.total_score = total_score

def selection_sort(arr, key=lambda x: x, reverse=False):
    n = len(arr)
    for i in range(n):
        extreme = i
        for j in range(i+1, n):
            if not reverse:
                if key(arr[j]) < key(arr[extreme]):
                    extreme = j
            else:
                if key(arr[j]) > key(arr[extreme]):
                    extreme = j
        arr[i], arr[extreme] = arr[extreme], arr[i]
    return arr


students = [
    Student("Иванов", "Алексей", 1980, [4, 5, 4, 5], 18),
    Student("Петров", "Борис", 1982, [3, 4, 3, 4], 14),
    Student("Сидоров", "Василий", 1981, [5, 5, 5, 5], 20),
    Student("Алексеев", "Григорий", 1983, [4, 3, 4, 3], 14),
    Student("Борисов", "Дмитрий", 1980, [3, 3, 4, 4], 14),
]

sorted_students = selection_sort(students, key=lambda s: s.last_name)
print("1. Фамилии по алфавиту:")
for student in sorted_students:
    print(student.last_name)

sorted_students = selection_sort(students, key=lambda s: s.last_name, reverse=True)
print("\n2. Фамилии в обратном порядке:")
for student in sorted_students:
    print(student.last_name)

sorted_students = selection_sort(students, key=lambda s: s.birth_year)
print("\n3. По старшинству (старшие первыми):")
for student in sorted_students:
    print(f"{student.last_name} ({student.birth_year} г.р.)")

sorted_students = selection_sort(students, key=lambda s: s.birth_year, reverse=True)
print("\n4. По старшинству (младшие первыми):")
for student in sorted_students:
    print(f"{student.last_name} ({student.birth_year} г.р.)")

sorted_students = selection_sort(students, key=lambda s: s.total_score)
print("\n5. По общему баллу (по возрастанию):")
for student in sorted_students:
    print(f"{student.last_name}: {student.total_score}")

sorted_students = selection_sort(students, key=lambda s: s.total_score, reverse=True)
print("\n6. По общему баллу (по убыванию):")
for student in sorted_students:
    print(f"{student.last_name}: {student.total_score}")

sorted_students = selection_sort(students, key=lambda s: s.grades[0])
print("\n7. По результатам 1-го экзамена (структуры):")
for student in sorted_students:
    print(f"{student.last_name}: {student.grades[0]}")

sorted_students = selection_sort(students, key=lambda s: s.grades[1], reverse=True)
print("\n8. По результатам 2-го экзамена (матан, по убыванию):")
for student in sorted_students:
    print(f"{student.last_name}: {student.grades[1]}")

sorted_students = selection_sort(students, key=lambda s: s.grades[2])
print("\n9. По результатам 3-го экзамена (физика):")
for student in sorted_students:
    print(f"{student.last_name}: {student.grades[2]}")

sorted_students = selection_sort(students, key=lambda s: s.grades[3], reverse=True)
print("\n10. По результатам 4-го экзамена (программирование, по убыванию):")
for student in sorted_students:
    print(f"{student.last_name}: {student.grades[3]}")

sorted_students = selection_sort(students, key=lambda s: s.first_name)
print("\n11. Имена по алфавиту:")
for student in sorted_students:
    print(student.first_name)

sorted_students = selection_sort(students, key=lambda s: s.first_name, reverse=True)
print("\n12. Имена в обратном алфавитном порядке:")
for student in sorted_students:
    print(student.first_name)