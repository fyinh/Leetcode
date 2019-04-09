# coding=utf-8

"""
7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

# code
def fresult(x):
    l = list(str(x))
    l.reverse()
    result = int("".join(l))
    return result
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if (x > (2**31-1) or x < -2**31):
            return 0
        else:
            if (x < 0):
                x = abs(x)
                x = fresult(x)
                x -= 2*x
                if (x < -2**31):
                    return 0
                else:
                    return x
            else:
                if (fresult(x) > 2**31-1):
                    return 0
                else:
                    return fresult(x)