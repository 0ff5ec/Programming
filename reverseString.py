'''
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
'''
"""
        :type s: str
        :rtype: str
        """
class Solution(object):
    def reverseString(self, s):
        return s[::-1]

if __name__ == "__main__":
	sol = Solution()
	print(sol.reverseString(raw_input('Enter the string: ')))
