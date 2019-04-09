# coding=utf-8

"""
33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

o(logn) = 二分搜索
二分搜索法的关键在于获得了中间数后，
判断下面要搜索左半段还是右半段，
如果中间的数小于最右边的数，
则右半段是有序的，
若中间数大于最右边数，
则左半段是有序的，
只要在有序的半段里用首尾两个数组来判断目标值是否在这一区域内，
这样就可以确定保留哪半边了
"""

# code
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if (len(nums) == 0):
            return -1
        left = 0
        right = len(nums) - 1
        while (left <= right):
            mid = (left + right) / 2
            if (nums[mid] == target):
                return mid
            elif (nums[mid] < nums[right]):
                if (nums[mid] < target and nums[right] >= target):
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if (nums[left] <= target and nums[mid] > target):
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

