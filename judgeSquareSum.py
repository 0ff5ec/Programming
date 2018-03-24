#   -*-   coding:  utf-8    -*-
'''
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:
Input: 3
Output: False
'''
"""
        :type c: int
        :rtype: bool
        """
import math
class Solution(object):
    def judgeSquareSum(self, c):
        if int(math.sqrt(c))**2 == c:
            return True
        else:
            i = 1
            while i <= c-i*i:
                if int(math.sqrt(c-i*i))**2 == c-i*i:
                    return True
                else:
                    i += 1
            return False

if __name__ == "__main__":
	sol = Solution()	
	print(sol.judgeSquareSum(int(raw_input('Enter the sum: '))))
