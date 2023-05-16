# Ascending
def mergeSort(arr):
    middle = len(arr)//2
    leftList =arr[:middle]
    rightList = arr[middle:]
    # Recursievly calling mergesort until the length of array is 1
    if len(arr) > 1:
        mergeSort(leftList)
        mergeSort(rightList)
    i=0
    j=0
    k=0
    # Sorting
    while i < len(leftList) and j < len(rightList):
        if leftList[i] < rightList[j]:
            arr[k] = leftList[i]
            i +=1
            k+=1
        else:
            arr[k] = rightList[j]
            j+=1
            k+=1
    # To add the leftout items from the left sublist
    while i < len(leftList):
        arr[k] = leftList[i]
        i +=1
        k+=1
    # To add the leftout items from the right sublist
    while j < len(rightList):
        arr[k] = rightList[j]
        j +=1
        k+=1
    return arr
        
arr = [5,2,66,34,1,444,87,0,34,-1,90,-34]
result = mergeSort(arr)
print(result)




# Descending
def mergeSortDesc(arra):
    middle = len(arra)//2
    leftHalf = arra[:middle]
    rightHalf = arra[middle:]
    if len(arra) >1:
        mergeSortDesc(leftHalf)
        mergeSortDesc(rightHalf)
    i=0
    j=0
    k=0
    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] > rightHalf[j]:
            arra[k] = leftHalf[i]
            i+=1
            k+=1
        else:
            arra[k] = rightHalf[j]
            j+=1
            k+=1
    while i < len(leftHalf):
        arra[k] = leftHalf[i]
        i+=1
        k+=1
    while j < len(rightHalf):
        arra[k] = rightHalf[j]
        j+=1
        k+=1
    return arra

    
arra = [5,2,66,34,1,444,87,0,34,-1,90,-34]
result1 = mergeSortDesc(arra)
print(result1)