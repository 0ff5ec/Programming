'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
'''
"""
        :type num: int
        :rtype: bool
        """
class Solution(object):
    def isPowerOfFour(self, num):
        if num < 1:
            return False
        if (num**(0.5))%1 != 0:
            return False
        num = int(num**(0.5))
        return not num & (num-1)

if __name__ == "__main__":
	sol = Solution()
	print(sol.isPowerOfFour(int(raw_input('Enter the number: '))))
