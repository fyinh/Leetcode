# coding=utf-8

"""
49. Group Anagrams

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

"""

# code
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strs_map = {}
        res = []
        for s in strs:
            tmp = ''.join(sorted(s))
            if tmp in strs_map:
                strs_map[tmp].append(s)
            else:
                strs_map[tmp] = [s]
        for s_list in strs_map.values():
            res.append(s_list)
        return res