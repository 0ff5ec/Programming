#    -*-    coding: utf-8    -*-
'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
"""
        :type num1: str
        :type num2: str
        :rtype: str
        """
class Solution:
    def multiply(self, num1, num2):
        product = [0] * (len(num1) + len(num2))
        idx = len(product)-1
        for n1 in reversed(num1):
            tmpIndex = idx
            for n2 in reversed(num2):
                product[tmpIndex] += int(n1) * int(n2)
                product[tmpIndex-1] += product[tmpIndex]/10
                product[tmpIndex] %= 10
                tmpIndex -= 1
            idx -= 1
        leadingZeros = 0
        while leadingZeros < len(product)-1 and product[leadingZeros] == 0:
            leadingZeros += 1
        return ''.join(map(str,product[leadingZeros:]))

if __name__ == "__main__":
	sol = Solution()	
	print(sol.multiply(raw_input('Enter num1: '),raw_input('Enter num2: ')))
