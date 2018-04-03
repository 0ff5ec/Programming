#    -*-    coding: utf-8    -*-
'''
Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

For example, Given s = “eceba”,

T is "ece" which its length is 3.
'''
"""
        :type s: str
        :rtype: int
        """
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        sub = ""
        i , cnt = 0 , 0 # input: eceeebaaaaaa
        maxSubLen = 0
        while i < len(s):
            if s[i] not in sub:
                if cnt < 2:
                    idx = i
                    cnt += 1
                    sub += s[i]
                else:
                    maxSubLen = max(maxSubLen, len(sub))
                    sub = s[idx:i]
                    sub = sub + s[i]
                    idx = i
                i += 1
            else:
                if sub[-1] != s[i]:
                    idx = i
                sub += s[i]
                i += 1
        return max(maxSubLen, len(sub))

if __name__ == "__main__":
	sol = Solution()
	print(sol.lengthOfLongestSubstringTwoDistinct(raw_input('Enter a string: ')))
