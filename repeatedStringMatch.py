#   -*-   coding: utf-8   -*-
'''
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
'''
"""
        :type A: str
        :type B: str
        :rtype: int
        """
class Solution:
    def repeatedStringMatch(self, A, B):
        if B in A:
            return 1
        i = 1
        s = A
        while len(s) < len(B):
            s = s+A
            i += 1
            if B in s:
                return i
        if B in s+A:
            return i+1
        return -1

if __name__ == "__main__":
	sol = Solution()
	print(sol.repeatedStringMatch(raw_input('Enter A: '),raw_input('Enter B: ')))
