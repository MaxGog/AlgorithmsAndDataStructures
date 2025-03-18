def linear_search(arr, key):
    comparisons = 0
    for num in arr:
        comparisons += 1
        if num == key:
            return num, comparisons
    return None, comparisons

def binary_search(arr, key):
    comparisons = 0
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if arr[mid] == key:
            return arr[mid], comparisons
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return None, comparisons

def create_index_table(arr, step):
    index_table = []
    for i in range(0, len(arr), step):
        index_table.append((i, arr[i]))
    return index_table


def index_sequential_search(arr, key, step):
    comparisons = 0
    index_table = create_index_table(arr, step)
    
    for i in range(len(index_table) - 1):
        comparisons += 1
        if index_table[i][1] <= key < index_table[i + 1][1]:
            low = index_table[i][0]
            high = index_table[i + 1][0]
            break
    else:
        comparisons += 1
        low = index_table[-1][0]
        high = len(arr) - 1

    for i in range(low, high + 1):
        comparisons += 1
        if arr[i] == key:
            return arr[i], comparisons
    return None, comparisons

arr = list(map(int, input("Введите элементы массива через пробел (массив должен быть упорядочен): ").split()))
key = int(input("Введите ключ для поиска: "))

result, comparisons = linear_search(arr, key)
if result is not None:
    print(f"Линейный поиск: элемент {result} найден, число сравнений: {comparisons}")
else:
    print(f"Линейный поиск: элемент не найден, число сравнений: {comparisons}")

result, comparisons = binary_search(arr, key)
if result is not None:
    print(f"Бинарный поиск: элемент {result} найден, число сравнений: {comparisons}")
else:
    print(f"Бинарный поиск: элемент не найден, число сравнений: {comparisons}")

step = int(input("Введите шаг для индексно-последовательного поиска: "))
result, comparisons = index_sequential_search(arr, key, step)
if result is not None:
    print(f"Индексно-последовательный поиск: элемент {result} найден, число сравнений: {comparisons}")
else:
    print(f"Индексно-последовательный поиск: элемент не найден, число сравнений: {comparisons}")