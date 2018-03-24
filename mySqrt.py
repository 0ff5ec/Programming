#    -*- coding: utf-8   -*-
'''
Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.


Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we want to return an integer, the decimal part will be truncated.
'''
"""
        :type x: int
        :rtype: int
        """
class Solution(object):
    def mySqrt(self, x):
        if x == 0:
            return 0
        elif x < 4:
            return 1
        i = 2
        while i*i <= x:
            i += 1
        return i-1

if __name__ == "__main__":
	sol = Solution()
	print(sol.mySqrt(int(raw_input('Enter the number: '))))
