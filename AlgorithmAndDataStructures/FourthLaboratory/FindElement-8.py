import random
import time

def linear_random_search(arr, target):
    comparisons = 0
    start_time = time.time()
    
    shuffled_arr = arr.copy()
    random.shuffle(shuffled_arr)
    
    for i in range(len(shuffled_arr)):
        comparisons += 1
        if shuffled_arr[i] == target:
            end_time = time.time()
            return shuffled_arr[i], comparisons, end_time - start_time
    
    end_time = time.time()
    return None, comparisons, end_time - start_time

def binary_random_search(arr, target):
    comparisons = 0
    start_time = time.time()
    
    shuffled_arr = sorted(arr.copy())
    random.shuffle(shuffled_arr)
    sorted_arr = sorted(shuffled_arr)
    
    left, right = 0, len(sorted_arr) - 1
    
    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        
        if sorted_arr[mid] == target:
            end_time = time.time()
            return sorted_arr[mid], comparisons, end_time - start_time
        elif sorted_arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    end_time = time.time()
    return None, comparisons, end_time - start_time

def indexed_sequential_random_search(arr, target):
    comparisons = 0
    start_time = time.time()
    
    n = len(arr)
    group_size = 3
    indices = []
    elements = []
    
    shuffled_arr = arr.copy()
    random.shuffle(shuffled_arr)
    
    for i in range(0, n, group_size):
        comparisons += 1
        if i + group_size <= n:
            elements.append(shuffled_arr[i])
            indices.append(i)
        else:
            elements.append(shuffled_arr[i])
            indices.append(i)
    
    random.shuffle(elements)
    for i in range(len(elements)):
        comparisons += 1
        if elements[i] >= target:
            start_idx = indices[i]
            end_idx = min(start_idx + group_size, n)
            for j in range(start_idx, end_idx):
                comparisons += 1
                if shuffled_arr[j] == target:
                    end_time = time.time()
                    return shuffled_arr[j], comparisons, end_time - start_time
            break
    
    end_time = time.time()
    return None, comparisons, end_time - start_time

def get_array_from_input():
    try:
        n = int(input("Введите количество элементов массива: "))
        if n <= 0:
            raise ValueError("Количество элементов должно быть положительным")
            
        print(f"\nВведите {n} чисел:")
        arr = []
        for i in range(n):
            num = float(input(f"Элемент {i+1}: "))
            arr.append(num)
            
        return arr
    except ValueError as e:
        print(f"\nОшибка: {str(e)}")
        return None

print("Задание №8: Поиск элементов случайным образом помощью линейного, бинарного и индексно-последовательного поиска.")
arr = get_array_from_input()
    
try:
    target = float(input("\nВведите искомое число: "))
except ValueError:
    print("\nОшибка: неверный формат числа")
    
print("\nРезультаты поиска:")

linear_result, linear_comparisons, linear_time = linear_random_search(arr, target)
print(f"\nЛинейный случайный поиск:")
print(f"Результат: {linear_result}")
print(f"Количество сравнений: {linear_comparisons}")
print(f"Время выполнения: {linear_time:.6f} секунд")

binary_result, binary_comparisons, binary_time = binary_random_search(arr, target)
print(f"\nБинарный случайный поиск:")
print(f"Результат: {binary_result}")
print(f"Количество сравнений: {binary_comparisons}")
print(f"Время выполнения: {binary_time:.6f} секунд")

indexed_result, indexed_comparisons, indexed_time = indexed_sequential_random_search(arr, target)
print(f"\nИндексно-последовательный случайный поиск:")
print(f"Результат: {indexed_result}")
print(f"Количество сравнений: {indexed_comparisons}")
print(f"Время выполнения: {indexed_time:.6f} секунд")