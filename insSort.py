# arr = [2, 1, 6, 7, 3, 4]
# arr = [9, 8, 7, 6, 5, 4]
# arr = [1, 2, 3, 4, 5, 6]
arr = [9, 4]

# print(arr[i])


def ins_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


ins_sort(arr)
print(arr)
