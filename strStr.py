'''
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
'''
"""
        :type haystack: str
        :type needle: str
        :rtype: int
        """
class Solution:
    def strStr(self, haystack, needle):
        l_needle = len(needle)
        if needle == "":
            return 0
        if l_needle > len(haystack):
            return -1
        for i in range(len(haystack)):
            if needle[0] == haystack[i]:
                if needle == haystack[i:i+l_needle]:
                    return i
        return -1
if __name__ == "__main__":
	haystack = "mississipi"
	needle = "issip"
	sol = Solution()
	print(sol.strStr(haystack,needle))
