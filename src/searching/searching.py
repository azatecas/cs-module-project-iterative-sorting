# liner complexity 0(n)
def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if target == arr[i]:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
#binary search has a O(log(n)) logrithmic complexity
def binary_search(arr, target):

    # Your code here
    min = 0
    max = len(arr) - 1 #larget index in arr

    while min <= max:
        mid = (min + max) // 2 #floor division
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            min = mid + 1
        else:
            max = mid - 1


    return - 1  # not found
