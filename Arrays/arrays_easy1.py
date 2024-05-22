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

print(sorted_squared([-4,-2,0,1,3]))