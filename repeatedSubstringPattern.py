#   -*-   coding: utf-8   -*-
'''
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
Example 1:
Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.
Example 2:
Input: "aba"

Output: False
Example 3:
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
'''
"""
        :type s: str
        :rtype: bool
        """
class Solution:
    def repeatedSubstringPattern(self, s):
        if not s:
            return False
        dup = (s*2)[1:-1]
        return s in dup

if __name__ == "__main__":
	sol = Solution()
	print(sol.repeatedSubstringPattern(raw_input('Enter the string: ')))
