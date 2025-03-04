def linear_search(arr):
    min_element = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_element:
            min_element = arr[i]
    return min_element

def binary_search(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
            
    return arr[left]

def index_sequential_search(arr):
    min_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i
    return arr[min_idx]


print("Задание №1: Найти наименьший элемент в упорядоченном массиве А с помощью линейного, бинарного и индексно-последовательного поиска.")
print("Заполните массив, для окончания ввода введите 'e'")
arr = []
while True:
    element = input("Введите значение элемента: ")
    if element.lower() == "e":
            break
    arr.append(int(element))

print(f"Исходный массив: {arr}")
print(f"\nРезультаты поиска:")
print(f"Линейный поиск: {linear_search(arr)}")
print(f"Бинарный поиск: {binary_search(arr)}")
print(f"Индексно-последовательный поиск: {index_sequential_search(arr)}")

