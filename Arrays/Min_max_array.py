"""
Given an array, write functions to find the minimum and maximum elements in it. 
"""

#timne complexity is O(nlogn)
def min_max(array):
    first = 0
    array1 = []
    last = len(array) - 1
    array1 = array.sort()
    min = array[first]
    max = array[last]
    return min,max

#print(min_max([100,500,200,1,233]))


# solving the same problem in O(n)

def min_max(arr):
    """Return the minimum and maximum elements in an unsorted array."""
    min_val = arr[0]
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
        if arr[i] > max_val:
            max_val = arr[i]
    return min_val, max_val


print(min_max([100,500,200,1,233]))