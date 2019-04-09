# coding=utf-8

"""
47. Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

注意数组数字有重复，我选择最后去一下重

"""

# code
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        result = []
        self.dfs(nums,[],res)
        for i in res:
            if i not in result:
                result.append(i)
        return result
    def dfs(self, nums,path,res):
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:],path+[nums[i]],res)
        if len(nums)==0:
            res.append(path)
