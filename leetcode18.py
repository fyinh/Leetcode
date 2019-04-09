# coding=utf-8

"""
18. 4Sum

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

# code
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) <= 3:
            return  []
        nums = sorted(nums)
        four = []
        for i in range(0, len(nums)-3):
            if nums[i] == nums[i-1] and i != 0:
                continue
            for j in range(i+1, len(nums)-2):
                if nums[j] == nums[j-1] and j != i+1:
                    continue
                t = target-nums[i]-nums[j]
                l,r = j+1,len(nums)-1
                while l<r:
                    s = nums[r]+nums[l]
                    if s == t:
                        four.append([nums[i],nums[j],nums[l],nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif s < t:
                        l += 1
                    else:
                        r -= 1
        return four
