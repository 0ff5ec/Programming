#    -*-    coding: utf-8    -*-
'''
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
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
'''
"""
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
class Solution(object):
    def divide(self, dividend, divisor):
        f1, f2 = 0, 0
        if dividend < 0: f1 = 1
        if divisor < 0: f2 = 1
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            tmp, i = divisor, 1
            while dividend >= tmp:
                dividend -= tmp
                res += i
                i <<= 1
                tmp <<= 1
        if f1^f2:
            res = -res
        return min(max(-2147483648, res), 2147483647)

if __name__ == "__main__":
	sol = Solution()
	print(sol.divide(int(raw_input('Enter dividend: ')),int(raw_input('Enter divisor: '))))
