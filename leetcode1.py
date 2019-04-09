# coding=utf-8

"""
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

# code
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if (nums[i] > target):
                pass
            for j in range(i+1,len(nums)):
                if (nums[j] > target):
                    pass
                if ((nums[j] + nums[i]) == target):
                    rtype = [i,j]
                    return rtype