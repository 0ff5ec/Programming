# -*- coding: utf-8 -*-
'''
Given an integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:
Input: -1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
'''
"""
        :type num: int
        :rtype: int
        """
class Solution(object):
    def findComplement(self, num):
        if num < 0:
            l = 31
            num = num + 2147483648
        else:
            l = len(bin(num)) - 2
        s = '0b'
        for i in range(l):
            s += '1'
        return num^int(s,2)

if __name__ == "__main__":
	sol = Solution()
	print(sol.findComplement(int(raw_input('Enter the number: '))))

