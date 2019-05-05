# coding=utf-8

"""
77. Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

回溯法
"""

# code
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        nums = range(1, n+1)
        self.generate(nums, k, res, [])
        return res

    def generate(self,nums, k, res, path):
        if k > len(nums):
            return
        if k == 0:
            res.append(path)
        else:
            for i in range(len(nums)):
                self.generate(nums[i+1:], k-1, res, path+[nums[i]])

