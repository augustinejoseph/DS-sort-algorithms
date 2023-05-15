def bubbleSort(arr):
    for i in range(0, len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("Basic bubble sort",arr)


arr = [5,2,66,34,1,444,87,0,34,-1,90,-34]
bubbleSort(arr)


# Descending
def bubbleSortDesc(arr1):
    for i in range(len(arr1)-1, -1):
        for j in range(len(arr1)-1, -1, 0):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    print(arr)

arr1 = [5,2,66,34,1,444,87,0,34,-1,90,-34]
bubbleSortDesc(arr)