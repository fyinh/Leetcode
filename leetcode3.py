# coding=utf-8

"""
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

# code
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # s = "pwwkew"
        ls = []
        l = list(s)
        lenl = len(l)
        chars = []

        for i in range(lenl):
            if (len(chars) == 0):
                chars.append(l[i])
            elif l[i] == chars[-1]:
                ls.append(len(chars))
                chars = []
                chars.append(l[i])
            elif(l[i] in chars):
                ind = chars.index(l[i])
                ls.append(len(chars))
                chars = chars[ind+1:]
                chars.append(l[i])
            else:
                chars.append(l[i])
        ls.append(len(chars))
        ls = list(set(ls))

        return max(ls)