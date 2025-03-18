def linear_search(arr):
    """Линейный поиск чисел больше 50"""
    result = []
    for num in arr:
        if num > 50:
            result.append(num)
    return result

def binary_search(arr):
    """Бинарный поиск чисел больше 50"""
    sorted_arr = sorted(arr)
    result = []
    
    def binary_find(start, end):
        if start >= end:
            return
        
        mid = (start + end) // 2
        if sorted_arr[mid] > 50:
            result.append(sorted_arr[mid])
            
        binary_find(start, mid)
        binary_find(mid + 1, end)
    
    binary_find(0, len(sorted_arr))
    return sorted(result)

def indexed_sequential_search(arr):
    """Индексно-последовательный поиск чисел больше 50"""
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
        if elements[i] > 50:
            start_idx = indices[i]
            end_idx = min(start_idx + group_size, n)
            for j in range(start_idx, end_idx):
                if arr[j] > 50:
                    result.append(arr[j])
    
    return sorted(list(set(result)))


print("Задание №6: Вывести на экран сообщение, каких чисел больше относительно 50 в упорядоченной таблице с помощью линейного, бинарного и индексно-последовательного поиска.")
arr = list(map(int, input("Введите элементы массива через пробел (массив должен быть упорядочен): ").split()))
print("\nРезультаты поиска:")
print(f"\nЛинейный поиск: {linear_search(arr)}")
print(f"Бинарный поиск: {binary_search(arr)}")
print(f"Индексно-последовательный поиск: {indexed_sequential_search(arr)}")
