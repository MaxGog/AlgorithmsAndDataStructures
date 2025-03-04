def linear_search(arr):
    result = []
    for num in arr:
        if num > 30:
            result.append(num)
    return result

def binary_search(arr):
    def find_first_greater():
        left, right = 0, len(arr) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > 30:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return result
    
    first_idx = find_first_greater()
    if first_idx == -1:
        return []
        
    return arr[first_idx:]

def index_sequential_search(arr):
    result = []
    i = 0
    while i < len(arr):
        if arr[i] > 30:
            result.append(arr[i])
        i += 1
            
    return result



print("Задание №2: Найти элементы в упорядоченном массиве А, которые больше 30, с помощью линейного, бинарного и индексно-последовательного поиска.")
print("Заполните массив, для окончания ввода введите 'e'")
arr = []
while True:
    element = input("Введите значение элемента: ")
    if element.lower() == "e":
            break
    arr.append(int(element))

print(f"\nВведенный массив: {arr}")
print(f"Элементы больше 30:")
print(f"Линейный поиск: {linear_search(arr)}")
print(f"Бинарный поиск: {binary_search(arr)}")
print(f"Индексно-последовательный поиск: {index_sequential_search(arr)}")