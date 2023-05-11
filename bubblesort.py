def bubbleSort(arr):
    for i in range(0, len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("Basic bubble sort",arr)


arr = [5,2,66,34,1,444,87,0,34,-1,90,-34]
bubbleSort(arr)
