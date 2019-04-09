# coding=utf-8

"""
6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""

# code
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if (numRows == 1):
            return s
        slen = len(s)
        res = [""]*slen
        # print len(res)
        # print res[0]
        k = 0
        interval = numRows * 2 -2
        j = 0
        while(j<slen):
            res[k] = s[j]
            k += 1
            j += interval
        # print res
        for i in range(1,numRows-1):
            inter = interval - 2 * i
            j = i
            while(j<slen):
                res[k] = s[j]
                k += 1
                j += inter
                inter = interval - inter
        # print res
        j = numRows - 1
        while (j<slen):
            res[k] = s[j]
            k += 1
            j += interval
        # print res
        result = "".join(res)
        return result
