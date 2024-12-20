'''
Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.

Example:
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merge_dicts(dict1, dict2)

Output:
{'a': 1, 'b': 5, 'c': 7, 'd': 5}
'''
def merge_dicts_1(dicts1: dict, dicts2: dict) -> dict: # Time complexity: O(n) & Space complexity: O(n)
    for key in dicts1:
        if key in dicts2:
            dicts2[key] += dicts1[key]
        else:
            dicts2[key] = dicts1[key]
    return dicts2

# method 2 using built-in function copy() to merge two dictionaries
def merge_dicts_2(dict1, dict2): # Time complexity: O(n+m) & Space complexity: O(n+m)
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result

# method 3 using built-in function collections.Counter() to merge two dictionaries
from collections import Counter
def merge_dicts_3(dict1, dict2): # Time complexity: O(n+m) & Space complexity: O(n+m)
    return dict(Counter(dict1) + Counter(dict2))

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(merge_dicts_1(dict1, dict2)) # Output: {'a': 1, 'b': 5, 'c': 7, 'd': 5}
print(merge_dicts_2(dict1, dict2)) # Output: {'a': 1, 'b': 5, 'c': 7, 'd': 5}
print(merge_dicts_3(dict1, dict2)) # Output: {'a': 1, 'b': 5, 'c': 7, 'd': 5}

