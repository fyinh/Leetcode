# coding=utf-8

"""
59. Spiral Matrix II

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

"""

# code
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        matrix=[[0]*n for _ in range(n)]
        num = 1
        left, right, top, buttom = 0, len(matrix[0])-1, 0, len(matrix)-1
        while left <= right and top <= buttom:
            for i in range(left, right+1):
                matrix[top][i] = num
                num += 1
            for j in range(top+1, buttom):
                matrix[j][right] = num
                num += 1
            for k in reversed(range(left,right+1)):
                if top < buttom:
                    matrix[buttom][k] = num
                    num += 1
            for m in reversed(range(top+1,buttom)):
                if left < right:
                    matrix[m][left] = num
                    num += 1
            left += 1
            right -= 1
            top += 1
            buttom -= 1
        return matrix