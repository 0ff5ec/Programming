#  -*- coding: utf-8 -*-
'''
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
'''
"""
        :type s: str
        :rtype: int
        """
class Solution(object):
    def titleToNumber(self, s):
        i = 0
        ans = 0
        while i < len(s):
            ans += (ord(s[-i-1]) - 64)*(26**i)
            i += 1
        return ans

if __name__ == "__main__":
	sol = Solution()
	print(sol.titleToNumber(raw_input('Enter excel title: ')))
