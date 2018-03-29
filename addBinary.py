#   -*-   coding:  utf-8    -*-
'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''
"""
        :type a: str
        :type b: str
        :rtype: str
        """
class Solution:
    def addBinary(self, a, b):
        return bin(int(a,2)+int(b,2))[2:]

if __name__ == "__main__":
	sol = Solution()
	print(sol.addBinary(raw_input('Enter a: '),raw_input('Enter b: ')))
