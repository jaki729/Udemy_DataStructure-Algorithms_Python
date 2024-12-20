''' 
Dictionary: 
It is Key-value pair, Unordered, Mutable, Indexed

How dictionary works:
- It is a collection of key-value pairs
- The key is used to identify the value
- The key must be unique
- The value can be anything

How dictionary are stored in memory:
- Dictionary are stored in hash tables
- The key is converted to a hash code using a hash function
- The hash code is used to store the key-value pair in a memory location
- The key is used to retrieve the value from the memory location

Hash tables:
- It is a data structure that stores key-value pairs

Hash function:
- It is a function that converts the key to a hash code

Hash code:
- It is a unique code generated by the hash function
- It is used to store the key-value pair in a memory location


'''
#  Update / add an element to the dictionary

myDict = {'name': 'Edy', 'age': 26}
myDict['address'] = 'London'
print(myDict)

#  Traverse through a dictionary

def traverseDict(dict):
    for key in dict:
        print(key, dict[key])

traverseDict(myDict)

#  Searching a dictionary


def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'The value does not exist'
print(searchDict(myDict, 27))

#  Dictionary methods

#  Delete or remove a dictionary

myDict.pop('name')

# using del keyword
del myDict['address']

# using popitem method
myDict.popitem() # remove the last item

# using clear method
myDict.clear()

# using copy method
# copy method returns a shallow copy of the dictionary
# A shallow copy means the copying process does not recurse on the nested objects
# The copied dictionary is a new dictionary
# Any changes made to the copied dictionary do not affect the original dictionary
# The copied dictionary is stored in a different memory location
# The copied dictionary is a separate object
myDict = {'name': 'Edy', 'age': 26}
myDict2 = myDict.copy()

# using dict method 
myDict3 = dict(myDict)

# Nested dictionary
myFamily = {
    'child1': {
        'name': 'Edy',
        'age': 26
    },
    'child2': {
        'name': 'John',
        'age': 20
    }
}
print(myFamily)

# using formkeys method
# The fromkeys method returns a new dictionary with the specified keys and values
# The fromkeys method takes two arguments: keys and values
# The keys argument is a sequence of keys for the new dictionary
# The values argument is optional. It is used to set the value of each key
# If the values argument is not specified, the value of each key is None
# Synatx: dict.fromkeys(keys, value) 
# keys: Required. The sequence of keys
# value: Optional. The value for all keys. Default value is None
# Return value: A new dictionary with the specified keys and values
# Example:
keys = {'a', 'b', 'c', 'd'}
value = 0
myDict4 = dict.fromkeys(keys, value)
print(myDict4)

# using get method
# The get method returns the value of the specified key
# The get method takes one argument: key
# The key argument is the key of the value to retrieve
# If the key exists, the get method returns the value of the key 
# If the key does not exist, the get method returns None
# Syntax: dict.get(key) 
# key: Required. The key of the value to retrieve
# Return value: The value of the specified key
# Example:
myDict = {'name': 'Edy', 'age': 26}
print(myDict.get('name'))

# using items method
# The items method returns a view object that displays a list of a dictionary's key-value tuple pairs
# The items method takes no arguments 
# Syntax: dict.items() 
# Return value: A view object that displays a list of a dictionary's key-value tuple pairs
# Example:
myDict = {'name': 'Edy', 'age': 26}
print(myDict.items())

# using keys method
# The keys method returns a view object that displays a list of a dictionary's keys
# The keys method takes no arguments 
# Syntax: dict.keys() 
# Return value: A view object that displays a list of a dictionary's keys 
# Example:
myDict = {'name': 'Edy', 'age': 26}
print(myDict.keys())

# using setdefault method
# The setdefault method returns the value of the specified key
# If the key does not exist, the setdefault method creates the key with the specified value
# The setdefault method takes two arguments: key and value
# Syntax: dict.setdefault(key, value) or dict.setdefault(key)
# key: Required. The key of the value to retrieve
# value: Optional. The value to return if the key does not exist
# Return value: The value of the specified key
# Example:
myDict = {'name': 'Edy', 'age': 26}
print(myDict.setdefault('name', 'John'))

# using update method
# The update method updates the dictionary with the specified key-value pairs
# The update method takes one argument: key-value pairs
# The key-value pairs argument is a dictionary containing the key-value pairs to update the dictionary
# Syntax: dict.update(key-value pairs) or dict.update(dict)
# key-value pairs: Required. A dictionary containing the key-value pairs to update the dictionary
# Return value: None
# Example:
myDict5 = {'name': 'Edy', 'age': 26}
myDict5.update({'address': 'London'})
print(myDict5)

# using values method
# The values method returns a view object that displays a list of a dictionary's values
# The values method takes no arguments
# Syntax: dict.values() 
# Return value: A view object that displays a list of a dictionary's values
# Example:
myDict = {'name': 'Edy', 'age': 26}
print(myDict.values())

# Dictionary operations

# using in operator
# The in operator returns True if the specified key is in the dictionary
# The in operator takes one argument: key
# Syntax: key in dict
# key: Required. The key to search for
# dict: Required. The dictionary to search in
# Return value: True if the specified key is in the dictionary, otherwise False
# Example:
myDict = {'name': 'Edy', 'age': 26}
print('name' in myDict)

# using not in operator
# The not in operator returns True if the specified key is not in the dictionary
# The not in operator takes one argument: key
# Syntax: key not in dict
# key: Required. The key to search for 
# dict: Required. The dictionary to search in
# Return value: True if the specified key is not in the dictionary, otherwise False
# Example:
myDict = {'name': 'Edy', 'age': 26}
print('name' not in myDict)

# using len function
# The len function returns the number of items in the dictionary
# The len function takes one argument: dictionary
# Syntax: len(dict)
# dict: Required. The dictionary to count the number of items
# Return value: The number of items in the dictionary
# Example:
myDict = {'name': 'Edy', 'age': 26}
print(len(myDict))

#using all function
# The all function returns True if all items in the dictionary are true
# The all function takes one argument: dictionary
# Syntax: all(dict)
# dict: Required. The dictionary to check if all items are true
# Return value: True if all items in the dictionary are true, otherwise False
# Example:
myDict = {'name': 'Edy', 'age': 26}
print(all(myDict))

# using any function
# The any function returns True if any item in the dictionary is true
# The any function takes one argument: dictionary
# Syntax: any(dict)
# dict: Required. The dictionary to check if any item is true
# Return value: True if any item in the dictionary is true, otherwise False
# Example:
myDict = {'name': 'Edy', 'age': 26}
print(any(myDict))

# sorted method
# The sorted method returns a sorted list of the specified dictionary keys
# The sorted method takes one argument: dictionary
# Syntax: sorted(dict)
# dict: Required. The dictionary to return the sorted keys
# Return value: A sorted list of the dictionary keys
# Example:
myDict = {'eooooa': 1, 'aas': 2, 'udd': 3, 'sseo': 4, 'werwi': 5}

print(sorted(myDict, key=len))

'''
Dictionary vs List
Dictionary:
- It is unordered
- It is mutable
- Access items by key
- Collection of key-value pairs
- Preferred whne the key is unique
- No duplicate keys

List:
- It is ordered
- It is mutable
- Access items by index
- Collection of elements
- Preferred when the order is important(oredered data)
- Duplicate elements are allowed
'''

'''
Dictionary comprehension
Dictionary comprehension is an elegant and concise way to create dictionaries
It is similar to list comprehension
newDict = {new_key:new_value for (key, value) in dict.items()}
newDict = {new_key:new_value for (key, value) in dict.items() if condition}
Example:
'''
# newDict = {new_key:new_value for (key, value) in dict.items()}
myDict = {'name': 'Edy', 'age': 26}
newDict = {k:v for (k, v) in myDict.items()}
print(newDict)

# newDict = {new_key:new_value for (key, value) in dict.items() if condition}
newDict = {k:v for (k, v) in myDict.items() if v != 26}
print(newDict)

import random
city_names = ["New York", "London", "Paris", "Tokyo"]
newDict = {city : random.randint(20, 30) for city in city_names}
print(newDict)
