#   -*-   coding:   utf-8   -*-
'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False
'''
"""
        :type num: int
        :rtype: bool
        """
class Solution(object):
    def isPerfectSquare(self, num):
        if num == 0 or num == 1:
            return True
        else:
            low = 2
            high = num
            middle = (2+num)//2
            while low < high:
                sqMiddle = middle*middle
                if sqMiddle == num:
                    return True
                elif sqMiddle > num:
                    high = middle - 1
                else:
                    low = middle + 1
                middle = (high + low)//2
            return True if middle*middle == num else False

if __name__ == "__main__":
	sol = Solution()
	print(sol.isPerfectSquare(int(raw_input('Enter the number: '))))
