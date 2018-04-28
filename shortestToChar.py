#    -*-    coding: utf-8    -*-
'''
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
'''
"""
        :type S: str
        :type C: str
        :rtype: List[int]
        """
class Solution(object):
    def shortestToChar(self, S, C):
        prev = float('-inf')
        dist = []
        for i, x in enumerate(S):
            if x == C:
                prev = i
            dist.append(i - prev)
        prev = float('inf')
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C:
                prev = i
            dist[i] = min(dist[i], prev - i)

        return dist

if __name__ == "__main__":
	sol = Solution()
	print(sol.shortestToChar(raw_input('Enter S: '),raw_input('Enter C: ')))
