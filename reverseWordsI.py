#    -*-    coding: utf-8    -*-
'''
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.
Clarification:
What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.
'''
"""
        :type s: str
        :rtype: str
        """
class Solution(object):
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])

if __name__ == "__main__":
	sol = Solution()
	print(sol.reverseWords(raw_input('Enter string: ')))

