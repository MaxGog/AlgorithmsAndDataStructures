def linear_search(arr):
    multiples_of_three = []
    for num in arr:
        if num % 3 == 0:
            multiples_of_three.append(num)
    return multiples_of_three

def binary_search(arr):
    arr.sort()
    multiples_of_three = []
    for i in range(len(arr)):
        if arr[i] % 3 == 0:
            multiples_of_three.append(arr[i])
    return multiples_of_three

def indexed_sequential_search(arr):
    n = len(arr)
    group_size = 3
    indices = []
    elements = []
    
    for i in range(0, n, group_size):
        if i + group_size <= n:
            elements.append(arr[i])
            indices.append(i)
        else:
            elements.append(arr[i])
            indices.append(i)
    
    multiples_of_three = []
    for i in range(len(elements)):
        if elements[i] % 3 == 0:
            start_idx = indices[i]
            end_idx = start_idx + group_size if start_idx + group_size <= n else n
            for j in range(start_idx, end_idx):
                if arr[j] % 3 == 0:
                    multiples_of_three.append(arr[j])
    return sorted(list(set(multiples_of_three)))


print("Задание №3: Вывести на экран все числа массива А кратные 3 (3,6,9,...) с помощью линейного, бинарного и индексно-последовательного поиска.")
n = int(input("Введите количество элементов массива: "))
arr = []
print(f"Введите {n} чисел:")
for i in range(n):
    num = int(input())
    arr.append(num)

print("\nЧисла, кратные 3 (линейный поиск):")
print(linear_search(arr))

print("\nЧисла, кратные 3 (бинарный поиск):")
print(binary_search(arr.copy()))

print("\nЧисла, кратные 3 (индексно-последовательный поиск):")
print(indexed_sequential_search(arr))
