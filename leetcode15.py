# coding=utf-8

"""
15. 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.
"""

# code
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 暴力 o(n3)
        # res = []
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         tag = nums[i] + nums[j]
        #         if -tag in nums:
        #             k = nums.index(-tag)
        #             if (k != i and k != j):
        #                 tag_list =sorted([nums[i],nums[j],nums[k]])
        #                 if tag_list not in res:
        #                     res.append(tag_list)
        # return res

        res = [[1,1,1]]
        nums = sorted(nums)
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            begin = i + 1
            end = len(nums) -1
            while begin < end:
                cnt = nums[begin] + nums[end] + nums[i]
                if cnt == 0:
                    tag = [nums[i],nums[begin],nums[end]]
                    if tag != res[len(res)-1]:
                        res.append(tag)
                    begin += 1
                    end -= 1
                elif cnt < 0:
                    begin += 1
                else:
                    end -= 1
        return res[1:]