# coding=utf-8

"""
29. Divide Two Integers

Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:
Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

set:
用移位来做，移p位就相当于乘了2p

f(24,5)=24/5=20/5+4/5=4+0=4

5左移2位就是20，而左移3位就是40超过了24，因此第一部分商为22=4.

对余数4再进行分析，发现5不需要移位就比4大，因此第二部分商为0.

加和可得，商为4.
"""

# code
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if ((dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)):
            flag = -1
        else:
            flag = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        tag = 0
        while(dividend > divisor):
            shift = 0
            part = 1
            while(dividend > (divisor << shift)):
                part <<= 1
                shift += 1
            if (dividend == (divisor << shift)):
                tag += part
                break
            else:
                part >>= 1
                shift -= 1
            dividend -= divisor << shift
            tag += part
        if (dividend == divisor):
            tag += 1
        res = tag * flag
        if (res > 2**31-1 or res < -2**31):
            return 2**31-1
        else:
            return res

