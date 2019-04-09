# coding=utf-8

"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

# code
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = [-1,-1]
        # if(len(nums) == 0):
        #     return [-1,-1]
        left = 0
        right = len(nums) - 1
        while (left <= right):
            mid = (left + right) / 2
            if (nums[mid] == target):
                index[0] = mid
                index[1] = mid
                while(index[1] < len(nums) and nums[index[1]] == target):
                    index[1] += 1
                while(index[0] >= 0 and nums[index[0]] == target):
                    index[0] -= 1

            elif (nums[mid] < target):
                left = mid + 1
            else:
                right = mid - 1
        return index

