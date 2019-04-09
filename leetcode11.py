# coding=utf-8

"""
11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""

# code
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        maxs = 0
        while l < r:
            tag = min(height[l], height[r]) * (r - l)
            if (tag > maxs):
                maxs = tag
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxs