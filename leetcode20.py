# coding=utf-8

"""
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""

# code
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pars = [None]
        # print len(pars)
        parmap = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in parmap and parmap[c] == pars[len(pars)-1]:
                pars.pop()
            else:
                pars.append(c)
        return len(pars) == 1
