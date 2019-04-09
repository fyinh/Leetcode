# coding=utf-8

"""
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

动态规划 max[nums[i],nums[i] + tag_max[i-1]
"""

# code
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tag_max = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > (nums[i] + tag_max[i-1]):
                tag_max.append(nums[i])
            else:
                tag_max.append(nums[i] + tag_max[i-1])

        return max(tag_max)