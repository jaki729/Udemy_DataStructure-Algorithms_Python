# Searching algorithms - Linear Search
# The time complexity of the linear search is O(n), where n is the number of elements in the array.
# Space complexity is O(1) because we are using a constant amount of space.
# Linear search is rarely used practically because 
# other search algorithms such as the binary search algorithm and hash tables 
# allow significantly faster searching comparison to Linear search.

def linearSearch(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1



print(linearSearch([20,40,30,50,90], 90))