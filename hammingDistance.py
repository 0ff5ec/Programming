# -*- coding: utf-8 -*-
'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
'''
"""
        :type x: int
        :type y: int
        :rtype: int
        """
class Solution(object):
    def hammingDistance(self, x, y):
        res = x^y
        cnt = 0
        while res != 0:
            if res%2 != 0:
                cnt += 1
            res = res//2
        return cnt

if __name__ == "__main__":
	sol = Solution()
	print(sol.hammingDistance(int(raw_input('Enter number1: ')),int(raw_input('Enter number2: '))))
