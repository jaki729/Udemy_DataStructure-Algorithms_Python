'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example :

Input: nums = [1,2,3,1]
Output: true
Use: set()
'''
def contains_duplicate(nums):
    return len(nums) != len(set(nums))

# Test the function
print(contains_duplicate([1,2,3,1])) # True
print(contains_duplicate([1,2,3,4])) # False
