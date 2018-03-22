# -*- coding: utf-8 -*-
'''
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
'''
"""
        :type s: str
        :rtype: str
        """
class Solution(object):
    def reverseWords(self, s):
        s = s.split(" ")
        ret = ""
        for i in range(len(s)):
            ret += s[i][::-1] + " "
        return ret.rstrip()

if __name__ == "__main__":
	sol = Solution()
	print(sol.reverseWords(raw_input('Enter string: ')))
