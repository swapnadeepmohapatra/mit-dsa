def sort(arr):
    for right in range(1, len(arr)):
        left = right - 1
        elem = arr[right]

        while left >= 0 and arr[left] > elem:
            arr[left + 1] = arr[left]
            left -= 1
        arr[left + 1] = elem

    return arr


arr = [1, 2, 6, 3, 7, 5, 9]
print(sort(arr))
