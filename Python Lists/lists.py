# A list is a collection of items. The items can be integers, strings, another list, etc. A list is created by placing all the items (elements) inside square brackets [] , separated by commas. It can have any number of items and they may be of different types (integer, float, string etc.). A list can even have another list as an item. This is called a nested list.
# List are ordered collection and are mutable. This means that items in a list can be accessed using an index, and the contents of a list can be changed by using an assignment operator.
#list index starts from 0 to n-1 where n is the number of elements in the list.

# Accessing/Traversing the list

shoppingList = ['Milk', 'Cheese', 'Butter']

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]+"+"
    # print(shoppingList[i])
empty = []
for i in empty:
    print("I am empty")


# Update/Insert - List 

myList = [1,2,3,4,5,6,7]
print(myList)
myList.insert(4,15)

myList.append(55)

newList = [11,12,13,14]
myList.extend(newList)
print(myList)

#slicing a list
myList = [10,20,30,40,50,60,70,80,90]
print(myList[1:5]) # [20,30,40,50]
print(myList[1:5:2]) # [20,40]
print(myList[:5]) # [10,20,30,40,50]
print(myList[5:]) # [60,70,80,90]
print(myList[:]) # [10,20,30,40,50,60,70,80,90]

# Deleting an element from the list
myList = [10,20,30,40,50,60,70,80,90]
del myList[1] # deletes the element at index 1
print(myList) # [10,30,40,50,60,70,80,90]
myList.remove(90) # removes the element with value 90
print(myList) # [10,30,40,50,60,70,80]
myList.pop(2) # removes the element at index 2
print(myList) # [10,30,50,60,70,80]
myList.clear() # removes all the elements from the list
print(myList) # []

#  Searching for an element in the List
myList =  [10,20,30,40,50,60,70,80,90]

def searchinList(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return 'The value does not exist in the list'

print(searchinList(myList, 100))

#Linear Search method 1
list = [1,2,3,4,5,6,7,8,9,10]
def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1
print(linear_search(list, 10))
#output: 9

#Linear Search method 2 using enumerate
list = [1,2,3,4,5,6,7,8,9,10]
def linear_search(list, target):
    for index, value in enumerate(list):
        if value == target:
            return index
    return -1
print(linear_search(list, 10))
#output: 9


#  List operations / functions
a = [1,2,3,4,5]
b = [6,7,8,9,10]
c = a + b
print(c) # [1,2,3,4,5,6,7,8,9,10]
d = a * 3
print(d) # [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
print(len(a)) # 5
print(max(a)) # 5
print(min(a)) # 1
print(sum(a)) # 15

#built-in functions
list = [1,2,3,4,5,6,7,8,9,10]
#append() - Adds an element at the end of the list
def appendElement(list, element):
    list.append(element)
    return list
print(appendElement(list, 11))
#output: [1,2,3,4,5,6,7,8,9,10,11]

#clear() - Removes all the elements from the list
def clearList(list):
    list.clear()
    return list
print(clearList(list))
#output: []

#copy() - Returns a copy of the list
def copyList(list):
    return list.copy()
print(copyList(list))
#output: [1,2,3,4,5,6,7,8,9,10]

#count() - Returns the number of elements with the specified value
def countElement(list, value):
    return list.count(value)
print(countElement(list, 10))
#output: 1
list = [1,2,3,4,5,6,7,8,9,10,10,10]
print(countElement(list, 10))
#output: 3

#extend() - Add the elements of a list (or any iterable), to the end of the current list
def extendList(list, iterable):
    list.extend(iterable)
    return list
print(extendList(list, [11,12,13,14,15]))
#output: [1,2,3,4,5,6,7,8,9,10,10,10,11,12,13,14,15]

#index() - Returns the index of the first element with the specified value
list = [1,2,3,4,5,6,7,8,9,10]
def indexElement(list, value):
    return list.index(value)
print(indexElement(list, 10))
#output: 9
#print(indexElement(list, 15))
#output: ValueError: 15 is not in list

#insert() - Adds an element at the specified position
def insertElement(list, position, value):
    list.insert(position, value)
    return list
print(insertElement(list, 5, 15))
#output: [1,2,3,4,5,15,6,7,8,9,10]

#pop() - Removes the element at the specified position
def popElement(list, position):
    list.pop(position)
    return list
print(popElement(list, 5))
#output: [1,2,3,4,5,6,7,8,9,10] 15 is removed

#remove() - Removes the first item with the specified value
list = [1,2,3,4,5,6,7,8,9,10,10,10]
def removeElement(list, value):
    list.remove(value)
    return list
print(removeElement(list, 10))
#output: [1,2,3,4,5,6,7,8,9,10,10]

#reverse() - Reverses the order of the list
def reverseList(list):
    list.reverse()
    return list
print(reverseList(list))
#output: [10,9,8,7,6,5,4,3,2,1]

#sort() - Sorts the list
list = [1,3,2,5,4,6,8,7,10,9]
def sortList(list):
    list.sort()
    return list
print(sortList(list))
#output: [1,2,3,4,5,6,7,8,9,10]

#Without using list and doing operations
# total = 0 
# count = 0
# while (True):
#     inp = input('Enter a number: ') 
#     if inp == 'done': break
#     value = float(inp)
#     total = total + value
#     count = count + 1 
# average = total / count
# print('Average:', average)

#Using list and doing operations
numlist = []
while (True):
    inp = input('Enter a number: ') 
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)					
average = sum(numlist) / len(numlist) 
print('Average:', average)

#Strings and Lists
abc = 'With three words'
stuff = abc.split()
print(stuff) # ['With', 'three', 'words']
print(len(stuff)) # 3
print(stuff[0]) # With
for w in stuff:
    print(w)
#output: With three words
str = "spam-spam1-spam2"
delimiter = '-'
str.split(delimiter)
print(str.split(delimiter))
#output: ['spam', 'spam1', 'spam2']

#Joining a list of strings into a single string
list = ['With', 'three', 'words']
delimiter = ' '
delimiter.join(list)
print(delimiter.join(list))
#output: With three words

#Shuffling a list
fruit=['apple', 'banana', 'papaya', 'cherry']
import random
random.shuffle(fruit)
print(fruit)
#output: ['banana', 'apple', 'papaya', 'cherry']

#Everytime take the copy of the list and then do the operations
#else the original list will be modified

#Arrays vs Lists

#Similarities:
#Both are used to store data
#Both are mutable
#They can be indexed and iterated
#They can be sliced

#Differences:
#Arrays can store only homogeneous data whereas lists can store heterogeneous data
#Arrays are faster and require less memory
#Arrays support vectorised operations, while lists don't


#List Comprehension
#List comprehension is an elegant way to define and create lists based on existing lists.
#List comprehension is generally more compact and faster than normal functions and loops for creating list.
#Syntax: new_list = [expression for_loop_one_or_more conditions]
#Example:
#Create a list of squares of numbers from 0 to 9
squares = [i * i for i in range(10)]
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#Syntax with if condition: new_list = [expression for_loop_one_or_more conditions]
#Example:
#Create a list of even numbers from 0 to 9
evens = [i for i in range(10) if i % 2 == 0]
print(evens) # [0, 2, 4, 6, 8]
#Syntax with if else condition: new_list = [expression if condition else expression for_loop_one_or_more conditions]
#Example:
#Create a list of even numbers and odd numbers
evenodd = ['Even' if i % 2 == 0 else 'Odd' for i in range(10)]
print(evenodd) # ['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']
#Syntax with nested if condition: new_list = [expression for_loop_one_or_more conditions for_loop_one_or_more conditions]
#Example:
#Create a list of numbers from 0 to 9 and print the numbers less than 5
numbers = [y for y in range(10) if y < 5]
print(numbers) # [0, 1, 2, 3, 4]
#Syntax with nested for loop: new_list = [expression for_loop_one_or_more conditions for_loop_one_or_more conditions]
#Example:
#Create a list of tuples where each tuple contains the number and its square
numbers = [(y, y * y) for y in range(10)]
print(numbers) # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81)]
#Example:
#Create a list of tuples where each tuple contains the number and its square only if the number is even
numbers = [(y, y * y) for y in range(10) if y % 2 == 0]
print(numbers) # [(0, 0), (2, 4), (4, 16), (6, 36), (8, 64)]
#Syntax with function: new_list = [expression for_loop_one_or_more conditions for_loop_one_or_more conditions if function]
#Example:
#Create a list of numbers from 0 to 9 and print the numbers less than 5 using a function
def less_than_five(x):
    return x < 5
numbers = [y for y in range(10) if less_than_five(y)]
print(numbers) # [0, 1, 2, 3, 4]