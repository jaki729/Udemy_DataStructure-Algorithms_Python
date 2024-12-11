'''
Write a program to find all the pairs integer in a given array whose sum is equal to a given number.
For example if the array is [1, 2, 3, 4, 5] and the given sum is 5 the pairs are:
(1, 4)
(2, 3)
Need to print only the indices of the pairs not the elements.
'''
# Worst case time complexity: O(n^2)
def two_sum_1(arr, target):
    pairs=[]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j]==target:
                pairs.append((i, j))
    return pairs

# test the function
print(two_sum_1([1, 2, 3, 4, 5], 5)) # [(0, 3), (1, 2)]
print(two_sum_1([1, 2, 3, 4, 5], 6)) # [(0, 4), (1, 3)]

# Best case time complexity: O(n)
def two_sum_2(arr, target):
    result = []
    dict = {}
    for i, integer in enumerate(arr):
        if target - integer in dict:
            result.append([dict[target - integer], i])
        dict[integer] = i
    return result

# Test the function
print(two_sum_2([1, 2, 3, 4, 5], 5)) # [[0, 3], [1, 2]]
print(two_sum_2([1, 2, 3, 4, 5], 6)) # [[0, 4], [1, 3]]