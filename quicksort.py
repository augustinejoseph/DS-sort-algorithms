# # Ascending
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    middle = [ x for x in arr if x == pivot]
    return quickSort(left) + middle + quickSort(right)

arr = [4,-1,6,44,23,-564, 65, -64,0,0,5,-1]
result = quickSort(arr)
print(result)


# Descending
def quickSortDesc(arra):
    if len(arra) <= 1:
        return arra
    upper =[]
    lower = []
    medium = []
    pivot = arra[len(arra)//2]
    for i in range(len(arra)):
        if arra[i] >  pivot:
            upper.append(arra[i])
        elif arra[i] < pivot:
            lower.append(arra[i])
        else:
            medium.append(arra[i])
    return quickSortDesc(upper)+ medium+ quickSortDesc(lower)

arra = [4,-1,6,44,23,-564, 65, -64,0,0,5,-1]
result1 = quickSortDesc(arra)
print(result1)