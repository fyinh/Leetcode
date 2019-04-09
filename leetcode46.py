# coding=utf-8

"""
46. Permutations

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

递归时候：不能remove，不然回复不到数组原来的样子，所以可以采用切片，
至于pop、remove、del这些方法用起来很繁琐，而且容易出问题
"""

# code
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        self.dfs(nums,[],res)
        return res
    def dfs(self, nums,path,res):
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:],path+[nums[i]],res)
        if len(nums)==0:
            res.append(path)

