#    -*-    coding:   utf-8    -*-
'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
"""
        :type num1: str
        :type num2: str
        :rtype: str
        """
class Solution(object):
    def addStrings(self, num1, num2):
        if num1 == "0":
            return num2
        elif num2 == "0":
            return num1
        else:
            result = []
            i = len(num1) - 1
            j = len(num2) - 1
            carry = 0
            while i > -1 and j > -1:
                result.append(str((int(num1[i]) + int(num2[j]) + carry)%10))
                carry = (int(num1[i]) + int(num2[j]) + carry)//10
                i = i-1
                j = j-1
            while i > -1:
                result.append(str((int(num1[i]) + carry)%10))
                carry = (int(num1[i]) + carry)//10
                i = i-1
            while j > -1:
                result.append(str((int(num2[j]) + carry)%10))
                carry = (int(num2[j]) + carry)//10
                j = j-1
            if carry:
                result.append(str(carry))
            return "".join(result[::-1])

if __name__ == "__main__":
	sol = Solution()
	print(sol.addStrings(raw_input('Enter num1: '),raw_input('Enter num2: ')))
