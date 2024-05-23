"""
Longest consecutive sequence in a given array
Given an unsorted array of integers nums return the length of the longest consecutive elements sequence.

You must write an algorithm in O(n) time

"""
def longestconsecutive(nums):
    s = set(nums)
    longest = 0
    for num in s:
        if num -1 not in s:
            curr = 1
            while num + 1 in s:
                curr += 1
                num +=1 
            
            longest = max(longest,curr)
    
    return longest

print(longestconsecutive([1,2,100,3,500,4]))
