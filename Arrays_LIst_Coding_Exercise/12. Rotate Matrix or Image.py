'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example:
matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
'''

def rotate(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] # Transpose the matrix

    # Reverse each row
    for row in matrix: # iterate over each row in the matrix
        row.reverse() 

    return matrix

# Test the function
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix)) # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]