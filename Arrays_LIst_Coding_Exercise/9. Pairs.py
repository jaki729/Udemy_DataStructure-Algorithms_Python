'''
Write a program to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.
Example:
pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
Output : ['2+5', '4+3', '3+4', '-2+9']
'''
def pair_sum(arr, target_sum):
    result = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                result.append(f"{arr[i]}+{arr[j]}")
    return result

# Test the function
print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7)) # ['2+5', '4+3', '3+4', '-2+9']