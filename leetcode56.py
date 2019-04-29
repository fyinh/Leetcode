# coding=utf-8

"""
56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

"""

# code
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        flag = [True] * len(intervals)
        for i in range(1, len(intervals)):
            if intervals[i].start <= intervals[i-1].end:
                intervals[i].start = intervals[i-1].start
                flag[i-1] = False
        res = []
        for j in range(len(flag)):
            if flag[j] == True:
                res.append(intervals[j])
        return res