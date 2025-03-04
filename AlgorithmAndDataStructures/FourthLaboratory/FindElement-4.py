def linear_search(arr):
    """Линейный поиск элементов с модулем больше 20 и меньше 50"""
    result = []
    for num in arr:
        if abs(num) > 20 and abs(num) < 50:
            result.append(num)
    return result

def binary_search(arr):
    """Бинарный поиск элементов с модулем больше 20 и меньше 50"""
    sorted_arr = sorted(arr)
    result = []
    
    def binary_find(start, end):
        if start >= end:
            return
        
        mid = (start + end) // 2
        if abs(sorted_arr[mid]) > 20 and abs(sorted_arr[mid]) < 50:
            result.append(sorted_arr[mid])
            
        binary_find(start, mid)
        binary_find(mid + 1, end)
    
    binary_find(0, len(sorted_arr))
    return sorted(result)

def indexed_sequential_search(arr):
    """Индексно-последовательный поиск элементов с модулем больше 20 и меньше 50"""
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
    
    result = []
    for i in range(len(elements)):
        if abs(elements[i]) > 20 and abs(elements[i]) < 50:
            start_idx = indices[i]
            end_idx = min(start_idx + group_size, n)
            for j in range(start_idx, end_idx):
                if abs(arr[j]) > 20 and abs(arr[j]) < 50:
                    result.append(arr[j])
    
    return sorted(list(set(result)))

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

print("Задание №4: Найти все элементы, модуль которых больше 20 и меньше 50 в упорядоченной таблице, с помощью с помощью линейного, бинарного и индексно-последовательного поиска.")
arr = get_array_from_input()
print("\nРезультаты поиска:")
print(f"\nЛинейный поиск: {linear_search(arr)}")
print(f"Бинарный поиск: {binary_search(arr)}")
print(f"Индексно-последовательный поиск: {indexed_sequential_search(arr)}")
