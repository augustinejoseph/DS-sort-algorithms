# Sorting Algorithms
Sorting algorithms are used to arrange a list of items in a specific order.  Here are some of the most common sorting algorithms:

## 1. Bubble Sort: 
This is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.

```python
def bubbleSort(arr):
    for i in range(0, len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("Basic bubble sort",arr)


arr = [5,2,66,34,1,444,87,0,34,-1,90,-34]
bubbleSort(arr)
```
The bubbleSort function takes an array arr as an argument, and uses two nested loops to iterate over the array. The outer loop runs from i=0 to i=len(arr)-2, and the inner loop runs from j=0 to j=len(arr)-2.

Inside the inner loop, the function checks if the current element arr[j] is greater than the next element arr[j+1]. If this is true, the two elements are swapped using tuple unpacking syntax arr[j], arr[j+1] = arr[j+1], arr[j], effectively moving the greater element towards the end of the array.

This process of swapping adjacent elements continues until the end of the array is reached. At this point, the largest element in the array is guaranteed to be in its correct sorted position at the end. The outer loop then repeats the process, but with the last element (which is already sorted) excluded.

After all iterations are complete, the sorted array is printed using the print statement with the message "Basic bubble sort".

For the given input array arr=[5,2,66,34,1,444,87,0,34,-1,90,-34], the function will return the sorted array [ -34, -1, 0, 1, 2, 5, 34, 34, 66, 87, 90, 444].

## 2. Selection Sort: 
This algorithm sorts an array by repeatedly finding the minimum element from the unsorted part of the array and putting it at the beginning.
```python
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
```
A loop is executed for each element in the list, except for the last one. This loop is used to find the smallest element in the remaining unsorted portion of the list.

The loop has a variable index that keeps track of the index of the smallest element found so far. Initially, it is set to the current index of the loop.


Another nested loop is executed that starts from the next element after the current element in the outer loop and iterates till the end of the list.


If an element smaller than the current smallest element is found, its index is stored in the index variable.

After this loop completes, the smallest element is swapped with the element at the current index of the outer loop. This ensures that the smallest element is placed at its correct position in the sorted portion of the list.


Above steps are repeated till all elements in the list have been sorted.
The sorted list is returned as output.

## 3. Insertion Sort: 
This algorithm builds the final sorted array one item at a time. It iterates through an input array, removing one element at a time, and inserting it into a new, sorted array at the correct position.
```python
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
```
The for loop iterates over the list arr, starting from the second element (index 1) and going up to the last element (index len(arr)-1).

For each element arr[i] in the unsorted part of the list, the while loop compares it to the previous element arr[i-1]. If arr[i] is smaller than arr[i-1], then the two elements are swapped using the Python tuple syntax arr[i], arr[i-1] = arr[i-1], arr[i]. This swaps the elements in-place, without needing to create a temporary variable.

After the swap, the while loop continues to compare the swapped element to the previous element until it reaches the beginning of the sorted part of the list or finds an element that is smaller than it.

Once the while loop has finished, the current element has been inserted into the correct position in the sorted part of the list.

The for loop continues to iterate over the remaining unsorted elements of the list, each time inserting the current element into the correct position in the sorted part of the list.

Once the for loop has finished, the entire list is sorted in ascending order.

## 4. Merge Sort: 
This is a divide and conquer algorithm that divides an array into two halves, sorts the two halves separately, and then merges the sorted halves back together.
```python
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
```
The mergeSort function first finds the middle of the arrat by calculating middle = len(arr) // 2. This will be used to divide the array into two halves.

LeftList containing elements from the start of the array up to the middle index, and rightList containing elements from the middle index to the end of the array are created.

Then the mergeSort function is recursively called on leftList and rightList until their lengths become 1 or less. This effectively divides the array into smaller subarrays until each subarray has only one element.

Initialize variables i, j, and k to keep track of indices for the subarrays. i represents the index of leftList, j represents the index of rightList, and k represents the index of the merged array arr.

Perform the merging process to combine the sorted subarrays into a single sorted array. Compare the elements at leftList[i] and rightList[j], and place the smaller element in arr[k]. Increment the respective indices and k accordingly.

After the initial merging, check if any elements are left in either leftList or rightList. If so, add those remaining elements to arr to ensure all elements are included.

Finally, return the sorted arr.
## 5. Quick Sort: 
This is another divide and conquer algorithm that selects a "pivot" element and partitions the array around the pivot, such that elements smaller than the pivot come before it and elements larger than the pivot come after it. The algorithm then recursively sorts the subarrays on either side of the pivot.
```python
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    middle = [ x for x in arr if x == pivot]
    return quickSort(left) + middle + quickSort(right)

arr = [5,2,66,34,1,444,87,0,34,-1,90,-34]
result = quickSort(arr)
print(result)
```
The quickSort function first checks if the length of the input list arr is less than or equal to 1. If it is, then the list is already sorted and the function simply returns the list.

Otherwise, the function chooses a pivot element as the middle element of the list, using integer division (//) to ensure that the index is an integer.

The function then partitions the list into three sub-lists: left, right, and middle. The left list contains all the elements that are less than the pivot element, the right list contains all the elements that are greater than the pivot element, and the middle list contains all the elements that are equal to the pivot element.

The function recursively calls itself on the left and right sub-lists to sort them, and concatenates the sorted left, middle, and right lists to form the final sorted list.

The base case of the recursion is when the length of the input list is less than or equal to 1, which was handled in step 1.

## 6. Heap Sort: 
This algorithm uses a binary heap data structure to sort an array. It first builds a max heap from the array, then repeatedly extracts the maximum element and places it at the end of the array, until the array is sorted.