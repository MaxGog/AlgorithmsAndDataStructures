import time

def linear_search(arr, target):
    comparisons = 0
    start_time = time.time()
    
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            end_time = time.time()
            return i, comparisons, end_time - start_time
    
    end_time = time.time()
    return -1, comparisons, end_time - start_time

def binary_search(arr, target):
    comparisons = 0
    start_time = time.time()
    
    # Создаем отсортированную копию массива
    sorted_arr = sorted(arr)
    left, right = 0, len(sorted_arr) - 1
    
    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        
        if sorted_arr[mid] == target:
            # Находим исходную позицию в неотсортированном массиве
            for i in range(len(arr)):
                if arr[i] == target:
                    end_time = time.time()
                    return i, comparisons, end_time - start_time
        elif sorted_arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    end_time = time.time()
    return -1, comparisons, end_time - start_time

def indexed_sequential_search(arr, target):
    comparisons = 0
    start_time = time.time()
    
    n = len(arr)
    group_size = 3
    indices = []
    elements = []
    
    for i in range(0, n, group_size):
        comparisons += 1
        if i + group_size <= n:
            elements.append(arr[i])
            indices.append(i)
        else:
            elements.append(arr[i])
            indices.append(i)
    
    for i in range(len(elements)):
        comparisons += 1
        if elements[i] >= target:
            start_idx = indices[i]
            end_idx = min(start_idx + group_size, n)
            for j in range(start_idx, end_idx):
                comparisons += 1
                if arr[j] == target:
                    end_time = time.time()
                    return j, comparisons, end_time - start_time
            break
    
    end_time = time.time()
    return -1, comparisons, end_time - start_time


print("Задание 9: Дан список номеров машин (345, 368, 876, 945, 564, 387, 230), найти, на каком месте стоит машина с заданным номером, линейный, бинарный и индексно-последовательный поиск.")
target = [1, 2, 3, 4, 5, 6, 7]
car_numbers = [345, 368, 876, 945, 564, 387, 230]

print("\nРезультаты поиска:")

linear_pos, linear_comparisons, linear_time = linear_search(car_numbers, target)
print(f"\nЛинейный поиск:")
print(f"Позиция: {linear_pos}")
print(f"Количество сравнений: {linear_comparisons}")
print(f"Время выполнения: {linear_time:.6f} секунд")

binary_pos, binary_comparisons, binary_time = binary_search(car_numbers, target)
print(f"\nБинарный поиск:")
print(f"Позиция: {binary_pos}")
print(f"Количество сравнений: {binary_comparisons}")
print(f"Время выполнения: {binary_time:.6f} секунд")

indexed_pos, indexed_comparisons, indexed_time = indexed_sequential_search(car_numbers, target)
print(f"\nИндексно-последовательный поиск:")
print(f"Позиция: {indexed_pos}")
print(f"Количество сравнений: {indexed_comparisons}")
print(f"Время выполнения: {indexed_time:.6f} секунд")
