# coding=utf-8

"""
5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

# code
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        maxl = 0
        start = 0
        for i in xrange(n):
            if i - maxl >= 1 and s[i-maxl-1: i+1] == s[i-maxl-1: i+1][::-1]:
                start = i - maxl - 1
                maxl += 2
                continue
            if i - maxl >= 0 and s[i-maxl: i+1] == s[i-maxl: i+1][::-1]:
                start = i - maxl
                maxl += 1
        return s[start: start + maxl]