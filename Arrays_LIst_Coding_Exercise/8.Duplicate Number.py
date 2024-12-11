'''
Write a program that takes an array of numbers and returns the duplicate number from the array.
Example:
remove_duplicates([1, 1, 2, 2, 3, 4, 5])
Output : [1, 2, 3, 4, 5]
Example:
remove_duplicates([1, 2, 3, 4, 5])
Output : []
'''
# Time Complexity: O(n) and Space Complexity: O(n)
def remove_duplicates_1(lst):
    return list(set(lst))

# Test Cases
print(remove_duplicates_1([1, 1, 2, 2, 3, 4, 5])) # [1, 2, 3, 4, 5]


def remove_duplicates_2(lst):
    unique_list = []
    seen = set()
    for i in lst:
        if i not in seen:
            seen.add(i)
            unique_list.append(i)
    return unique_list

# Test Cases
print(remove_duplicates_2([7, 64, 7, 7, 7, 7, 7, 7, 7, 7])) # [7, 64]
print(remove_duplicates_2([1, 2, 3, 4, 5, 5, 5, 5, 5, 5])) # [1, 2, 3, 4, 5]