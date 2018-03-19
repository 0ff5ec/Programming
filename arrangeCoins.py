# -*- coding: utf-8 -*-
'''
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
'''
"""
        :type n: int
        :rtype: int
        """
class Solution(object):
    def arrangeCoins(self, n):
        if n == 0:
            return 0
        ret = 1
        while ret*(ret+1)/2 <= n:
            ret += 1
        return ret - 1

if __name__ == "__main__":
	sol = Solution()
	print(sol.arrangeCoins(int(raw_input('Enter number of coins: '))))
