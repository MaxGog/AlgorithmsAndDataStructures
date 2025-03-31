def print_menu():
    print("\nМеню:")
    print("1. Найти max/min элемент массива")
    print("2. Сортировка массива по убыванию")
    print("3. Создать новый массив с элементами по убыванию")
    print("4. Вставить число в упорядоченный массив")
    print("5. Перестроить массив из возрастания в убывание")
    print("6. Удалить отрицательные числа и отсортировать положительные")
    print("7. Формировать упорядоченный массив по мере ввода")
    print("8. Упорядочить список авторов по алфавиту")
    print("9. Создать список абонентов с сортировкой по номеру")
    print("10. Упорядочить слова по длине")
    print("11. Сортировка по модулям (возрастание/убывание)")
    print("12. Вставить числа между элементами отсортированного массива")
    print("0. Выход")

def task1():
    A = list(map(int, input("Введите элементы массива через пробел: ").split()))
    print(f"Максимальный элемент: {max(A)}")
    print(f"Минимальный элемент: {min(A)}")

def task2():
    A = list(map(int, input("Введите элементы массива через пробел: ").split()))
    A_sorted = sorted(A, reverse=True)
    print("Отсортированный массив:", A_sorted)

def task3():
    A = list(map(int, input("Введите элементы массива через пробел: ").split()))
    B = sorted(A, reverse=True)
    print("Новый массив B:", B)

def task4():
    A = sorted(list(map(int, input("Введите упорядоченный массив через пробел: ").split())))
    a = int(input("Введите число для вставки: "))
    
    # Находим позицию для вставки
    pos = 0
    while pos < len(A) and A[pos] < a:
        pos += 1
    
    A.insert(pos, a)
    print("Массив после вставки:", A)

def task5():
    A = sorted(list(map(int, input("Введите элементы массива через пробел: ").split())))
    A_reversed = sorted(A, reverse=True)
    print("Массив в порядке убывания:", A_reversed)

def task6():
    A = list(map(int, input("Введите элементы массива через пробел: ").split()))
    positive = sorted([x for x in A if x >= 0])
    print("Положительные числа по возрастанию:", positive)

def task7():
    A = list(map(int, input("Введите элементы массива через пробел: ").split()))
    B = []
    for num in A:
        B.append(num)
        B.sort()
        print(f"После добавления {num}: {B}")
    print("Итоговый упорядоченный массив B:", B)

def task8():
    A = input("Введите имена авторов через запятую: ").split(',')
    A = [name.strip() for name in A]
    A_sorted = sorted(A)
    print("Указатель авторов по алфавиту:")
    for author in A_sorted:
        print(author)

def task9():
    n = int(input("Введите количество абонентов: "))
    subscribers = []
    for i in range(n):
        phone = input(f"Введите номер телефона {i+1}: ")
        name = input(f"Введите фамилию {i+1}: ")
        subscribers.append((phone, name))
    
    # Сортировка по номеру телефона
    subscribers_sorted = sorted(subscribers, key=lambda x: x[0])
    print("\nСписок абонентов:")
    for phone, name in subscribers_sorted:
        print(f"{phone}: {name}")

def task10():
    A = input("Введите слова через пробел: ").split()
    A_sorted = sorted(A, key=lambda x: len(x))
    print("Слова по возрастанию длины:", A_sorted)

def task11():
    A = list(map(int, input("Введите элементы массива через пробел: ").split()))
    asc = sorted(A, key=lambda x: abs(x))
    desc = sorted(A, key=lambda x: abs(x), reverse=True)
    print("По возрастанию модулей:", asc)
    print("По убыванию модулей:", desc)

def task12():
    A = sorted(list(map(int, input("Введите элементы массива через пробел: ").split())))
    new_A = []
    for i in range(len(A)):
        new_A.append(A[i])
        if i < len(A) - 1:
            # Вставляем среднее значение между текущим и следующим элементом
            middle = (A[i] + A[i+1]) / 2
            new_A.append(middle)
    print("Массив с вставленными значениями:", new_A)

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