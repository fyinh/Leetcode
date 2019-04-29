# coding=utf-8

"""
62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28

solution: 排列组合问题，无顺序拿，也可以用动态规划
"""

# code
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        right = m - 1
        down = n - 1
        total = right + down
        first = 1
        second = 1
        while (down > 0):
            first *= total
            total -= 1
            second *= down
            down -= 1
        return first / second


# class Solution(object):
#     def uniquePaths(self, m, n):
#         """
#         :type m: int
#         :type n: int
#         :rtype: int
#         """
#         dp = [[0] * n for _ in range(m)]
#         dp[0][0] = 1
#         for i in range(0, m):
#             for j in range(0, n):
#                 if i > 0:
#                     dp[i][j] += dp[i-1][j]
#                 if j > 0:
#                     dp[i][j] += dp[i][j-1]
#         return dp[-1][-1]
