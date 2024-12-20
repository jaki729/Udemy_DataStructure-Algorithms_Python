'''
Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.

Example:
list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
check_same_frequency(list1, list2)
Output:
False
'''
def check_same_frequency_1(list1: list, list2: list) -> bool: # Time complexity: O(n) & Space complexity: O(n)
    frequency1 = {}
    frequency2 = {}
    for element in list1:
        frequency1[element] = frequency1.get(element, 0) + 1
    for element in list2:
        frequency2[element] = frequency2.get(element, 0) + 1
    return frequency1 == frequency2

# method 2 using built-in function collections.Counter() to check if two given lists have the same frequency of elements
from collections import Counter
def check_same_frequency_2(list1, list2): # Time complexity: O(n+m) & Space complexity: O(n+m)
    return Counter(list1) == Counter(list2)

# method 3 
def check_same_frequency_3(list1, list2):
    def frequency_counter(lst):
        frequency = {}
        for element in lst:
            frequency[element] = frequency.get(element,0) + 1
        return frequency
    return frequency_counter(list1) == frequency_counter(list2)

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
print(check_same_frequency_1(list1, list2)) # Output: False
print(check_same_frequency_2(list1, list2)) # Output: False
print(check_same_frequency_3(list1, list2)) # Output: False