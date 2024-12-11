'''
Write a function to find all pairs in a given integer array whose sum is equal to a given number.
The function takes two parameters: the array and the target sum value.
The function should return an array of arrays with the pairs.
Example
find_pairs([1, 2, 3, 4, 5], 5) # [[1, 4], [2, 3]]

Also program should return only unique pairs. If the array is [1, 2, 3, 4, 5] and the given sum is 5 the pairs are:
(1, 4)
(2, 3)
not:
(4, 1)
(3, 2)

Also the pairs like (2,2) and (3,3) are not allowed.
Exampe of (2,2) and (3,3) are not allowed
print(find_pairs([1, 2, 2, 3, 4, 5], 4)) # [[1, 3]]
print(find_pairs([1, 2, 3, 3, 4, 5], 6)) # [[1, 5], [2, 4]]
'''

def find_pairs(arr, target):
    pairs = []
    for i in range(len(arr)):
        for j in range(1+1, len(arr)):
            if arr[i] == arr[j]:
                continue
            elif arr[i] + arr[j] == target:
                pairs.append([arr[i], arr[j]])
    return pairs

# test the function
print(find_pairs([1, 2, 3, 4, 5], 5)) # [[1, 4], [2, 3]]
print(find_pairs([1, 2, 3, 4, 5], 6)) # [[1, 5], [2, 4]]
print(find_pairs([1, 2, 3, 4, 5], 7)) # [[2, 5], [3, 4]]
print(find_pairs([1, 2, 3, 4, 5], 8)) # []
print(find_pairs([1, 2, 2, 3, 4, 5], 4)) # [[1, 3]]
print(find_pairs([1, 2, 3, 3, 4, 5], 6)) # [[1, 5], [2, 4]]