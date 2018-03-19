# -*- coding: utf-8 -*-
'''
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.
Example 1:

Input:
26

Output:
"1a"
Example 2:

Input:
-1

Output:
"ffffffff"

'''
"""
        :type num: int
        :rtype: str
        """
class Solution(object):
    def toHex(self, num):
        sol = Solution()
        if num == 0:
            return "0"
        lookUp = {'10':'a', '11':'b', '12':'c', '13':'d', '14':'e', '15':'f'}
        s = ""
        if num > 0:
            while num != 0:
                if num%16 < 10:
                    s = str(num%16) + s
                else:
                    s = lookUp[str(num%16)] + s
                num = num//16
        else:
            return sol.toHex(int(bin(num & 0xffffffff), 2))
        return s

if __name__ == "__main__":
	sol = Solution()
	print(sol.toHex(int(raw_input('Enter the number: '))))
