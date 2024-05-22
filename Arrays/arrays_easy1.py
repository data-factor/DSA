"""
You are a given an array of integer in which each subsequent value is not less than the previous value.
Write a function that takes this array as an input and returns a new array with the squares of each number\
sorted in ascending order.
Test Cases
1. [1,3,5] ->  [1,9,25]
2. [0,5,6]-> [0,25,36]
3. [-4,-2,0,1,3] - > [0,1,4,9,16]
5. [] -> []
6. [2,3,3] -> [4,9,9]
"""
#brute Force method
#time complexity nlogn
def sorted_squared(array):
    if len(array) < 0:
        return array
    else:
        for element in range(len(array)):
            array[element] = array[element] ** 2
        array.sort()
        return array

#print(sorted_squared([-4,-2,0,1,3]))

#  Method 2
# Time = O(n) Space = O(n)
def sorted_squared(array):
    length = len(array)
    first,last = 0,length - 1
    result = [0] * length
    for element in reversed(range(length)):
        first_square = array[first] ** 2
        last_square = array[last] ** 2
        if first_square > last_square:
            result[element] = first_square
            first+= 1
        else:
            result[element] = last_square
            last-=1
    return result

print(sorted_squared([-5,-4,-2, 1, 9,12]))
