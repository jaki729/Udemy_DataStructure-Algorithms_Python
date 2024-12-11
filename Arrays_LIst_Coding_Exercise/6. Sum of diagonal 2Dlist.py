'''
Write a sum_diagonal function that takes a 2D list and returns the sum of the diagonal elements.
The diagonal elements are the elements that are in the same row and column.
Example:
sum_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) ➞ 15
# 1 + 5 + 9 = 15
'''
def sum_diagonal(lst):
    sum = 0
    for _ in range(len(lst)):
        sum += lst[_][_]
    return sum

# Test Cases
print(sum_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # 15