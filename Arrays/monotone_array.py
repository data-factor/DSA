"""
An array is monotonic if it is either montone increasing or monotone decreasing.
An array is monotone increasing if all its elements from left to right are non-decreasing.
An array is monotone decreasing if all its elements from left to right are non-increasing.
Given an integer array return true if the given array is montonic, or flase otherwise
Test case 
1. [1,2,3] Montonic increase True
2. [3,2,1] Montonic decreasee True
3. [3,3,4] True
4. [1,2,2] True
5. []      True
6. [2,2,3,1] False
"""

def monotonic_array(array):
    length = len(array)
    if length == 0: True
    first = array[0]
    last = array[length - 1]
    if first>last:
        for ele in range(length-1):
            if array[ele] < array[ele+1]: return False
    elif first == last:
            if array[ele]!=array[ele+1]: return False
    else:
         for k in range(length-1):
              if array[k] > array[k+1]: return False
    
    return True
                   
print(monotonic_array([1,2,3]))