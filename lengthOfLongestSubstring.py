#    -*-     coding: utf-8     -*-
'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
"""
        :type s: str
        :rtype: int
        """
class Solution:
    def lengthOfLongestSubstring(self, s):
        sub = ""
        maxSubLen , i= 0 , 0
        while i < len(s):
            if s[i] not in sub:
                sub = sub + s[i]
                i += 1
            else:
                maxSubLen = max(maxSubLen, len(sub))
                idx = sub.find(s[i])
                sub = sub[idx+1:] + s[i]
                i += 1
        return max(maxSubLen, len(sub))

if __name__ == "__main__":
	sol = Solution()
	s = "eceeeebbaaa"
	print(sol.lengthOfLongestSubstring(s))
