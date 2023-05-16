# Ascending
def selectionSort(arr):
    for i in range(len(arr)-1):
        index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[index]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]

    return arr

arr = [5,2,66,34,1,444,87,0,34,-1,90,-34]
result = selectionSort(arr)
print(result)



# Descending
def selectionSortDesc(arr1):
    for i in range(len(arra)-1):
        index = i
        for j in range(i+1, len(arra)):
            if arra[j] > arra[index]:
                index=j
        arra[i], arra[index] = arra[index], arra[i]
    return arra

arra = [5,2,66,34,1,444,87,0,34,-1,90,-34]
result1 = selectionSortDesc(arr)
print(result1)