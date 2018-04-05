#    -*-    coding: utf-8    -*-
'''
Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3.
'''
"""
        :type s: str
        :type k: int
        :rtype: int
        """
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        d = {}
        low, ret = 0, 0
        for i, c in enumerate(s):
            d[c] = i
            if len(d) > k:
                low = min(d.values())
                del d[s[low]]
                low += 1
            ret = max(i - low + 1, ret)
        return ret

if __name__ == "__main__":
	sol = Solution()
	print(sol.lengthOfLongestSubstringKDistinct(raw_input('Enter the string: '),int(raw_input('Enter k: '))))
