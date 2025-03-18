def linear_search(arr, target):
    """Линейный поиск с подсчетом сравнений"""
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return arr[i], comparisons
    return None, comparisons

def binary_search(arr, target):
    """Бинарный поиск с подсчетом сравнений"""
    comparisons = 0
    left, right = 0, len(arr) - 1
    
    while left <= right:
        comparisons += 1  # Считаем сравнение с mid
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return arr[mid], comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return None, comparisons

def indexed_sequential_search(arr, target):
    """Индексно-последовательный поиск с подсчетом сравнений"""
    comparisons = 0
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
                    return arr[j], comparisons
            break
    
    return None, comparisons


print("Задание №7: Найти элемент в упорядоченном массиве А и найти число сравнений помощью линейного, бинарного и индексно-последовательного поиска.")
arr = list(map(int, input("Введите элементы массива через пробел (массив должен быть упорядочен): ").split()))
    
try:
    target = float(input("\nВведите искомое число: "))
except ValueError:
    print("\nОшибка: неверный формат числа")
    
print("\nРезультаты поиска:")

linear_result, linear_comparisons = linear_search(arr, target)
print(f"\nЛинейный поиск:")
print(f"Результат: {linear_result}")
print(f"Количество сравнений: {linear_comparisons}")

binary_result, binary_comparisons = binary_search(arr, target)
print(f"\nБинарный поиск:")
print(f"Результат: {binary_result}")
print(f"Количество сравнений: {binary_comparisons}")

indexed_result, indexed_comparisons = indexed_sequential_search(arr, target)
print(f"\nИндексно-последовательный поиск:")
print(f"Результат: {indexed_result}")
print(f"Количество сравнений: {indexed_comparisons}")