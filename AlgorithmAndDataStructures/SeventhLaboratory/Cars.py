class Car:
    def __init__(self, number, brand, owner, last_repair_date, repair_due_date, previous_repairs=0):
        self.number = number
        self.brand = brand
        self.owner = owner
        self.last_repair_date = last_repair_date
        self.repair_due_date = repair_due_date
        self.previous_repairs = previous_repairs

def date_to_days(date):
    day, month, year = date
    return year * 365 + month * 30 + day

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

cars = [
    Car(1, "Жигули", "Иванов", (15, 5, 1995), (10, 8, 1996), 3),
    Car(2, "Мерседес", "Петров", (20, 6, 1994), (25, 7, 1996), 1),
    Car(3, "Жигули", "Сидоров", (10, 3, 1996), (5, 8, 1996), 2),
    Car(4, "Волга", "Алексеев", (5, 2, 1996), (30, 7, 1996), 0),
    Car(5, "Мерседес", "Борисов", (12, 4, 1995), (15, 9, 1996), 4),
]


sorted_cars = selection_sort(cars, key=lambda car: car.owner)
print("1. По алфавиту имен владельцев:")
for car in sorted_cars:
    print(f"{car.owner}: {car.brand} (№{car.number})")

sorted_cars = selection_sort(cars, key=lambda car: date_to_days(car.repair_due_date))
print("\n2. Порядок ремонта:")
for i, car in enumerate(sorted_cars, 1):
    print(f"{i}. {car.brand} (№{car.number}) - до {car.repair_due_date}")

zhiguli_cars = [car for car in cars if car.brand == "Жигули"]
sorted_cars = selection_sort(zhiguli_cars, key=lambda car: car.previous_repairs, reverse=True)
print("\n3. Жигули по убыванию ремонтов:")
for car in sorted_cars:
    print(f"{car.brand} (№{car.number}): {car.previous_repairs} ремонтов")

cars_with_2_repairs = [car for car in cars if car.previous_repairs == 2]
sorted_cars = selection_sort(cars_with_2_repairs, key=lambda car: car.number, reverse=True)
print("\n4. Машины с 2 ремонтами (по убыванию номеров):")
for car in sorted_cars:
    print(f"№{car.number}: {car.brand}")

no_repair_cars = [car for car in cars if car.previous_repairs == 0]
sorted_cars = selection_sort(no_repair_cars, key=lambda car: date_to_days(car.repair_due_date))
print("\n5. Машины без ремонтов по дате конца ремонта:")
for car in sorted_cars:
    print(f"№{car.number}: до {car.repair_due_date}")

mercedes_cars = [car for car in cars if car.brand == "Мерседес"]
sorted_cars = selection_sort(mercedes_cars, key=lambda car: car.owner, reverse=True)
print("\n6. Владельцы Мерседесов (обратный алфавит):")
for car in sorted_cars:
    print(car.owner)

august_1_1996 = date_to_days((1, 8, 1996))
early_cars = [car for car in cars if date_to_days(car.repair_due_date) < august_1_1996]
sorted_cars = selection_sort(early_cars, key=lambda car: car.brand)
print("\n7. Марки машин с ремонтом до 01.08.96:")
for car in sorted_cars:
    print(f"{car.brand} (до {car.repair_due_date})")

zhiguli_cars = [car for car in cars if car.brand == "Жигули"]
sorted_cars = selection_sort(zhiguli_cars, key=lambda car: car.number)
print("\n8. Номера Жигулей по возрастанию:")
for car in sorted_cars:
    print(f"№{car.number}")

last_year = 1995
owners = [car.owner for car in cars if car.last_repair_date[2] < last_year]
sorted_owners = selection_sort(owners)
print("\n9. Владельцы машин без ремонта с прошлого года:")
for owner in sorted_owners:
    print(owner)

next_month_cars = [car for car in cars if car.repair_due_date[1] == 8]  # август
sorted_cars = selection_sort(next_month_cars, key=lambda car: date_to_days(car.last_repair_date))
print("\n10. Машины к ремонту в следующем месяце:")
for car in sorted_cars:
    print(f"№{car.number}: последний ремонт {car.last_repair_date}")

owners_many_repairs = [car.owner for car in cars if car.previous_repairs > 3]
sorted_owners = selection_sort(owners_many_repairs, reverse=True)
print("\n11. Владельцы с >3 ремонтов (обратный алфавит):")
for owner in sorted_owners:
    print(owner)

mercedes_cars = [car for car in cars if car.brand == "Мерседес"]
sorted_cars = selection_sort(mercedes_cars, key=lambda car: car.number, reverse=True)
print("\n12. Номера Мерседесов по убыванию:")
for car in sorted_cars:
    print(f"№{car.number}")