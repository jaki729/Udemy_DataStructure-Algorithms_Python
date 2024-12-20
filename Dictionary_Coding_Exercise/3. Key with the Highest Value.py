'''
Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.

Example:
my_dict = {'a': 5, 'b': 9, 'c': 2}
max_value_key(my_dict))
Output:
b
'''
def max_key_value(my_dict: dict) -> str: # Time complexity: O(n) & Space complexity: O(1)
    max_key = max(my_dict, key=my_dict.get)
    return max_key

my_dict = {'a': 5, 'b': 9, 'c': 2}
print(max_key_value(my_dict)) # Output: b