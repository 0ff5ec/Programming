#   -*-   coding: utf-8    -*-
'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
'''
"""
        :type n: int
        :rtype: str
        """
class Solution(object):
    def convertToTitle(self, n):
        s = ""
        while n != 0:
            if n%26 == 0:
                s = 'Z' + s
                n = n//26 - 1
            else:
                s = chr(n%26 + 64) + s
                n = n//26
        return s

if __name__ == "__main__":
	sol = Solution()
	print(sol.convertToTitle(int(raw_input('Enter column number: '))))
