'''
Write a program to print the elements of a array except the first and last elements.
Example
middle([1, 2, 3, 4, 5]) # [2, 3, 4]
'''

def middle(arr):
    return arr[1:-1]

# test the function
print(middle([1, 2, 3, 4, 5])) # [2, 3, 4]