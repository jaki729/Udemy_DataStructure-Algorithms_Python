'''
Write a function that takes two list and returns True if one list is a permutation of the other.
Example :
list1 = [1,2,3]
list2 = [3,2,1]
Output: True

Example :
list1 = ["a","b","c"]
list2 = ["a","b","d"]
Output: False
'''


'''
Difference between sorted() and sort():
- sorted() returns a new sorted list from the elements of any iterable.
- sorted() does not modify the original list.
- sorted() by default sorts the list in ascending order.

- sorted() can take a reverse parameter to sort the list in descending order.
- sort() modifies the original list.
- sort() sorts the list in place.
'''
def is_permutation_1(list1, list2):
    return sorted(list1) == sorted(list2)

# Test the function
print(is_permutation_1([1,2,3], [3,2,1])) # True
print(is_permutation_1([1,2,3], [3,2,1,4])) # False

#using Counter()
'''
use of Counter() in Python:
- Counter() is a subclass of dictionary class.
- Counter() is used to count the frequency of elements in an iterable.
- Counter() returns a dictionary with elements as keys and their frequency as values.
- Counter() can be used with any iterable.
- Counter() is a part of the collections module.
- Counter() is an unordered collection.
'''
from collections import Counter
def is_permutation_2(list1, list2):
    return Counter(list1) == Counter(list2)

# Test the function
print(is_permutation_2(["s","a","m"], ["m","a","s"])) # True
print(is_permutation_2(["s","a","m"], ["m","a","s","t"])) # False
