# coding=utf-8

"""
67. Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

int()函数用于将一个字符串或数字转换为整型。语法：
class int(x, base)
x–字符串或数字
base–进制数，默认十进制。
bin()函数返回一个整型int或者长整数long int的二进制表示。
"""

# code
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a, 2)
        b = int(b ,2)
        return bin(a + b)[2:]