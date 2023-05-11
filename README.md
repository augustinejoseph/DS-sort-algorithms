# Sorting Algorithms
Sorting algorithms are used to arrange a list of items in a specific order.  Here are some of the most common sorting algorithms:

## Bubble Sort: 
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

## Selection Sort: 
This algorithm sorts an array by repeatedly finding the minimum element from the unsorted part of the array and putting it at the beginning.

## Insertion Sort: 
This algorithm builds the final sorted array one item at a time. It iterates through an input array, removing one element at a time, and inserting it into a new, sorted array at the correct position.

## Merge Sort: 
This is a divide and conquer algorithm that divides an array into two halves, sorts the two halves separately, and then merges the sorted halves back together.

## Quick Sort: 
This is another divide and conquer algorithm that selects a "pivot" element and partitions the array around the pivot, such that elements smaller than the pivot come before it and elements larger than the pivot come after it. The algorithm then recursively sorts the subarrays on either side of the pivot.

## Heap Sort: 
This algorithm uses a binary heap data structure to sort an array. It first builds a max heap from the array, then repeatedly extracts the maximum element and places it at the end of the array, until the array is sorted.