# Searching algorithms - Binary Search

# Binary search is a fast search algorithm with run-time complexity of Ο(log n). 
# Space complexity is O(1) because we are using a constant amount of space.
# This search algorithm works on the principle of divide and conquer. 
# For this algorithm to work properly, the data collection should be in the sorted form.

import math
def binarySearch(array, value):
    start = 0
    end = len(array)-1
    middle = math.floor((start+end)/2)
    while not(array[middle]==value) and start<=end:
        if value < array[middle]:
            end = middle - 1
        else:
            start = middle + 1 
        middle = math.floor((start+end)/2)
        # print(start, middle, end)
    if array[middle] == value:
        return middle
    else:
        return -1
        



custArray = [8, 9, 12, 15, 17, 19, 20, 21, 28]
print(binarySearch(custArray, 15))
# [8, 9, 12, 15, 17, 19, 20, 21, 28]
#  S              M               E
#  S  M      E
#        SM  E
#            SME