# Ascending
def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -=1
    return arr

arr = [4,-1,6,44,23,-564, 65, -64,0,0,5,-1]
result = insertionSort(arr)
print(result)


# Descending
def insertionSortDesc(arr):
    for k in range(1, len(arr)):
        a = k
        while a > 0 and arr[a] > arr[a-1]:
            arr[a], arr[a-1] = arr[a-1], arr[a]
            a -=1
    return arr

arr1 = [4,-1,6,44,23,-564, 65, -64,0,0,5,-1]
result1 = insertionSortDesc(arr1)
print(result1)