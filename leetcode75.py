# coding=utf-8

"""
75. Sort Colors

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""

# code
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        one_count = 0
        two_count = 0

        for i in nums:
            if i == 0:
                zero_count += 1
            elif i == 1:
                one_count += 1
            else:
                two_count += 1

        for i in range(zero_count):
            nums[i] = 0
        for i in range(zero_count, one_count+zero_count):
            nums[i] = 1
        for i in range(one_count+zero_count, one_count+zero_count+two_count):
            nums[i] = 2

