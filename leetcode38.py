# coding=utf-8

"""
38. Count and Say

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.



Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""

# code
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # n = 5
        if n == 1:
            return "1"
        else:
            count = 1
            s = "11#"
            while (count < n-1):
                letter_count = 1
                letter_tag = s[0]
                result_s = ""
                for i in range(1,len(s)):
                    if s[i] == letter_tag:
                        letter_count += 1
                    else:
                        result_s += str(letter_count)
                        result_s += s[i-1]
                        letter_count = 1
                        letter_tag = s[i]
                s = result_s + "#"
                count += 1
            res = s.replace("#","")
            return res

