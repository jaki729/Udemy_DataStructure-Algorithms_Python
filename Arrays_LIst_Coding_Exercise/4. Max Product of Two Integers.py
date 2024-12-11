'''
Write a program  to find the maximum product of two integers in a given array of integers.
Example
arr = [1, 7, 3, 4, 9, 5] 
max_product(arr) # Output: 63 (9*7)
'''
#Worst case time complexity: O(n^2)
def max_product_1(arr):
    max_product = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]*arr[j] > max_product:
                max_product = arr[i]*arr[j]
    return max_product

# Test the function
print(max_product_1([1, 7, 3, 4, 9, 5])) # 63

#Best case time complexity: O(n)
def max_product_2(arr):
    max1 = max(arr)
    arr.remove(max1)
    max2 = max(arr)
    return max1*max2

# Test the function
print(max_product_2([1, 7, 3, 4, 9, 5])) # 63

#Winthout using built in functions
def max_product_3(arr):
    if len(arr) < 2:
        return 0  

    max1 = float('-inf')  
    max2 = float('-inf')  

    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

    return max1 * max2

# Test the function
print(max_product_3([1, 7, 3, 4, 9, 5])) # 63