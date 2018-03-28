#   -*- coding: utf-8   -*-
'''
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5
'''
"""
        :type s: str
        :rtype: int
        """
class Solution(object):
    def countSegments(self, s):
        return len(s.split(" ")) - s.split(" ").count('')

if __name__ == "__main__":
	sol = Solution()
	print(sol.countSegments(raw_input('Enter segment: ')))
