# Ascending
def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -=1
    return arr

arr = [5,2,66,34,1,444,87,0,34,-1,90,-34]
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

arr1 = [5,2,66,34,1,444,87,0,34,-1,90,-34]
result1 = insertionSortDesc(arr1)
print(result1)