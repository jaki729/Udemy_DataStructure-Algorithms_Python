# What is Tuple?
# Tuple is a collection of items which is ordered and unchangeable. Tuples are written with round brackets.
# It is a immutable collection of items. 
# It is similar to List but the only difference 
# is that we can't change the elements of tuple once it is assigned whereas in the list, elements can be changed.

#  How to create a Tuple?

newTuple = ('a', 'b', 'c', 'd', 'e')
newTuple1 = tuple('abcde')

print(newTuple1)
'''              best case Average case
Creating a Tuple	O(1)	O(n)
Indexing	        O(1)	O(1)
Slicing	            O(1)	O(b - a)
Concatenation	    O(1)	O(k)
Traversal	        O(n)	O(n)

How tuple is located in memory?
Tuples are stored in a single block of memory.
So it is faster than list when it comes to indexing and slicing.
This is because the computer knows the exact position of the data in memory.

''' 

# Access Tuple elements

print(newTuple[0]) 

# Slice Tuple
print(newTuple[1:4])
print(newTuple[1:])
print(newTuple[:4])
print(newTuple[:])

#  Traverse through tuple

for i in newTuple:
    print(i)


for index in range(len(newTuple)):
    print(newTuple[index])


#  How to search for an element in Tuple?

print('a' in newTuple)
print('f' in newTuple)
# in oprtator uses linear search to find the element in tuple.
# So the time complexity is O(n) and space complexity is O(1)

#  How to search for an element in Tuple using index() method?
print(newTuple.index('a'))
# print(newTuple.index('f')) # ValueError: tuple.index(x): x not in tuple

def searchInTuple(pTuple, element): # time complexity is O(n) and space complexity is O(1)
    for i in pTuple:
        if i == element:
            return pTuple.index(i)
    return 'The element does not exist'

print(searchInTuple(newTuple, 'a'))

# Tuple Operations / Functions
myTuple = (1,4,3,2,5)
myTuple1 = (1,2,6,9,8,7)

print(myTuple + myTuple1) 
print(myTuple * 4)      
print(2 in myTuple1)

myTuple1.count(2)
myTuple1.index(2)

# Tuple Method tuple()
# The tuple() method is used to convert a list of items into a tuple.
# Syntax: tuple(iterable)
# The tuple() method takes a single parameter (iterable) and converts it into a tuple.
print(tuple([1,2,3,4,5])) # (1, 2, 3, 4, 5)

# Tuple Vs List
# Tuple is faster than list.
# Tuple is immutable whereas list is mutable.
# Tuple uses less memory than list.
# Tuple is used when we want to store the data that should not be changed.
# List is used when we want to store the data that can be changed.

# Function that can be used for both Tuple and List
# len(), max(), min(), sum(), all(), any()
# method cannot be used for Tuples are append(), remove(), pop(), insert(), clear(), sort(), reverse()
# Tuples can be stored as list elements 
# Tuples can be used when different data types
# Tuples are write protected