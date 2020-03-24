def getPeak(lst, l, r):
    left = l
    right = r
    mid = int(left + (right-left)/2)

    if len(lst) == 0:
        return lst[mid]
    elif lst[mid] >= lst[mid-1] or lst[mid] >= lst[mid+1]:
        return lst[mid]
    elif lst[mid] < lst[mid+1]:
        return getPeak(lst, mid+1, r)
    elif lst[mid] < lst[mid-1]:
        return getPeak(lst, l, mid-1)
    else:
        return "error"


testArray = [12, 16, 13, 12, 90, 78, 45]
print(getPeak(testArray, 0, len(testArray)-1))
