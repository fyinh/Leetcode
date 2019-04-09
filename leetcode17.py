# coding=utf-8

"""
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

# code
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        letter_dict = {2:["a","b","c"], 3:["d","e","f"], 4:["g","h","i"], 5:["j","k","l"], 6:["m","n","o"],
                       7:["p","q","r","s"], 8:["t","u","v"], 9:["w","x","y","z"]}
        if (digits == ""):
            return []
        else:
            res = []
            res = letter_dict[int(digits[0])]
            # print res
            for i in digits[1:]:
                tag = []
                for j in res:
                    for k in letter_dict[int(i)]:
                        flag = j + k
                        tag.append(flag)
                res = tag

            return res