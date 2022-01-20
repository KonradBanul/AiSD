def binary_search(numbers, value):
    first = 0
    end = len(numbers) - 1
    while first <= end:
        middle = (first + end) // 2
        if numbers[middle] is value:
            return middle
        if numbers[middle] < value:
            first = middle + 1
        elif numbers[middle] > value:
            end = middle - 1
    return -1

ints = [1, 5, 6, 7, 10, 26, 29, 40]
print(binary_search(ints, 7))
