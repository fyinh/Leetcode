# coding=utf-8

"""
74. Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""

# code
class Solution(object):
     def searchMatrix(self, matrix, target):
        if(matrix == [] or matrix == [[]]):
            return False
        for i in range(len(matrix)):
            if(target >= matrix[i][0] and target <= matrix[i][-1]):
                return target in matrix[i]
            if target < matrix[i][0]:
                break
        return False

