def print_menu():
    print("\nМеню:")
    print("1. Сортировка деталей на складе №1 (четные номера)")
    print("2. Поиск автомобилей с номерами, начинающимися на 4")
    print("3. Поиск 'счастливых' билетов")
    print("4. График ухода сотрудников на пенсию")
    print("5. Сортировка студентов по возрастанию общего балла")
    print("6. Автобусы с нечетными номерами по убыванию")
    print("7. Сортировка зарплат по убыванию")
    print("8. Автомобили со 'счастливыми' номерами")
    print("9. Выигрышные лотерейные билеты (сумма цифр делится на 4)")
    print("10. Поиск телефонных номеров 469***")
    print("11. Сортировка студентов по убыванию общего балла")
    print("12. Выигрышные билеты (первые 3 цифры = 8)")
    print("0. Выход")

def task1():
    details = [45, 56, 13, 75, 14, 18, 43, 11, 52, 12, 10, 36, 47, 9]
    warehouse1 = sorted([x for x in details if x % 2 == 0])
    print("Детали на складе №1:", warehouse1)

def task2():
    numbers = [456, 124, 786, 435, 788, 444, 565, 127, 458, 322, 411, 531, 400, 546, 410]
    filtered = sorted([x for x in numbers if str(x)[0] == '4'])
    print("Номера, начинающиеся на 4:", filtered)

def task3():
    tickets = [124512, 342351, 765891, 453122, 431350, 876432, 734626, 238651, 455734, 234987]
    lucky = sorted([t for t in tickets if sum(map(int, str(t)[:3])) == sum(map(int, str(t)[3:]))])
    print("Счастливые билеты:", lucky)

def task4():
    people = [("Иванов", 65), ("Петров", 60), ("Сидоров", 63), ("Козлов", 58), ("Смирнов", 67)]
    sorted_people = sorted(people, key=lambda x: x[1])
    print("График ухода на пенсию:", [name for name, age in sorted_people])

def task5():
    students = [("Иванов", [4,5,3,4,5]), ("Петров", [3,4,3,3,4]), ("Сидоров", [5,5,5,5,5])]
    sorted_students = sorted(students, key=lambda x: sum(x[1]))
    print("Студенты по возрастанию баллов:")
    for student in sorted_students:
        print(f"{student[0]}: {sum(student[1])}")

def task6():
    buses = [11, 32, 23, 12, 6, 52, 47, 63, 69, 50, 43, 28, 35, 33, 42, 56, 55, 101]
    odd_buses = sorted([b for b in buses if b % 2 != 0], reverse=True)
    print("Автобусы 2-го парка:", odd_buses)

def task7():
    salaries = {"Иванов": 166000, "Сидоров": 180000, "Петров": 150000, "Козлов": 200000}
    sorted_salaries = dict(sorted(salaries.items(), key=lambda x: x[1], reverse=True))
    print("Зарплаты по убыванию:")
    for name, salary in sorted_salaries.items():
        print(f"{name}: {salary}")

def task8():
    car_numbers = [1212, 3451, 7694, 4512, 4352, 8732, 7326, 2350, 4536, 2387, 5746, 6776, 4316, 1324]
    lucky_numbers = sorted([n for n in car_numbers if sum(map(int, str(n)[:2])) == sum(map(int, str(n)[2:]))], reverse=True)
    print("Автомобили со счастливыми номерами:", lucky_numbers)

def task9():
    tickets = [1234, 2345, 3456, 4567, 5678, 6789, 7890, 4321, 5432, 6543, 7654, 8765, 9876]
    winning = sorted([t for t in tickets if sum(map(int, str(t))) % 4 == 0], reverse=True)
    print("Выигрышные билеты:", winning)

def task10():
    phones = [456765, 469465, 469321, 616312, 576567, 469563, 567564, 469129, 675665, 469873, 569090, 469999, 564321, 469010]
    filtered = sorted([p for p in phones if str(p).startswith('469')], reverse=True)
    print("Номера 469***:", filtered)

def task11():
    students = [("Иванов", [4,5,3,4,5]), ("Петров", [3,4,3,3,4]), ("Сидоров", [5,5,5,5,5])]
    sorted_students = sorted(students, key=lambda x: sum(x[1]), reverse=True)
    print("Студенты по убыванию баллов:")
    for student in sorted_students:
        print(f"{student[0]}: {sum(student[1])}")

def task12():
    tickets = [1234, 2345, 3456, 4567, 5678, 6789, 7890, 4321, 5432, 6543, 7654, 8765, 9876, 8000, 7100]
    winning = sorted([t for t in tickets if sum(map(int, str(t)[:3])) == 8])
    print("Выигрышные билеты (первые 3 цифры = 8):", winning)

def main():
    while True:
        print_menu()
        choice = input("Выберите задание (0-12): ")
        
        if choice == '0':
            print("Выход из программы")
            break
        elif choice == '1':
            task1()
        elif choice == '2':
            task2()
        elif choice == '3':
            task3()
        elif choice == '4':
            task4()
        elif choice == '5':
            task5()
        elif choice == '6':
            task6()
        elif choice == '7':
            task7()
        elif choice == '8':
            task8()
        elif choice == '9':
            task9()
        elif choice == '10':
            task10()
        elif choice == '11':
            task11()
        elif choice == '12':
            task12()
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()