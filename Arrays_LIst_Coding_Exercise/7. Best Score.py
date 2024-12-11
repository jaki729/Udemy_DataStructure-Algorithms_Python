'''
Write a program that takes an array and returns the best score from the array only the first and second best scores are counted.
Example:
best_score([1, 2, 3, 4, 5]) ➞ [5, 4]
'''
#Worst Time Complexity: O(nlogn)
def best_score_1(lst):
    lst.sort(reverse=True)
    return [lst[0], lst[1]]

# Test Cases
print(best_score_1([1, 2, 3, 4, 5])) # [5, 4]
print(best_score_1([23, 45, 67, 89, 123])) # [123, 89]

#Best Time Complexity: O(n) with out usign built-in sort function
def best_score_2(lst):
    max1 = max2 = float('-inf')
    for i in lst:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2:
            max2 = i
    return [max1, max2]

# Test Cases
print(best_score_2([23, 45, 67, 89, 123, 123])) # [123, 123]
print(best_score_2([1, 2, 3, 4, 5])) # [5, 4]