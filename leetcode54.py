# coding=utf-8

"""
54. Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

记录 top buttom left right

"""

# code
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if matrix == []:
            return res
        left, right, top, buttom = 0, len(matrix[0])-1, 0, len(matrix)-1
        while left <= right and top <= buttom:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            for j in range(top+1, buttom):
                res.append(matrix[j][right])
            for k in reversed(range(left,right+1)):
                if top < buttom:
                    res.append(matrix[buttom][k])
            for m in reversed(range(top+1,buttom)):
                if left < right:
                    res.append(matrix[m][left])
            left += 1
            right -= 1
            top += 1
            buttom -= 1
        return res