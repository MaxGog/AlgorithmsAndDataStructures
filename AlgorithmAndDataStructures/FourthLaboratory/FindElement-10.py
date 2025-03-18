def linear_search(arr):
    result = []
    for num in arr:
        if num % 2 == 0:
            result.append(num)
    return result

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low


def find_all_even_binary(arr):
    result = []
    index = binary_search(arr, 2)
    while index < len(arr) and arr[index] % 2 == 0:
        result.append(arr[index])
        index += 1
    return result

def create_index_table(arr):
    index_table = []
    for i, num in enumerate(arr):
        if num % 2 == 0:
            index_table.append(i)
    return index_table


def index_sequential_search(arr, index_table):
    result = []
    for index in index_table:
        result.append(arr[index])
    return result

arr = list(map(int, input("Введите элементы массива через пробел (массив должен быть упорядочен): ").split()))

print("Линейный поиск:", linear_search(arr))

print("Бинарный поиск:", find_all_even_binary(arr))

index_table = create_index_table(arr)
print("Индексно-последовательный поиск:", index_sequential_search(arr, index_table))