#   -*-   coding: utf-8   -*-
'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
'''
"""
        :type s: str
        :rtype: int
        """
class Solution:
    def lengthOfLastWord(self, s):
        s = s.split(" ")
        i = 1
        while s[-i] == "" and i < len(s):
            i += 1
        if i > len(s):
            return 0
        return len(s[-i])

if __name__ == "__main__":
	sol = Solution()
	print(sol.lengthOfLastWord(raw_input('Enter the sentence: ')))
