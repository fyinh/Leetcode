# codingutf-8

"""
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

backtracking:
2 options:
add left
add right
2 restraints:
left == 0 not left
right == left not right
terminator:
left == right == 0

"""

# code
# Definition for singly-linked list.
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.generate(n, n, "", res)
        return res

    def generate(self, left, right, str, res):
        if left == 0 and right == 0:
            res.append(str)
            return
        if left > 0:
            self.generate(left - 1, right, str + '(', res)
        if right > left:
            self.generate(left, right - 1, str + ')', res)

