'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
"""
        :type x: int
        :rtype: int
        """
class Solution:
    def reverse(self, x):
        if x == 0 or x > 2147483648 or x < -2147483648:
            return 0
        elif x > 0 and x < 2147483648:
            tmp = str(x)
            s = ''
            for i in range(len(tmp)):
                s = s+tmp[-1-i]
            if int(s) > 2147483647:
                return 0
            return int(s)
        elif x < 0 and x > -2147483649:
            s = ''
            x = abs(x)
            tmp = str(x)
            for i in range(len(tmp)):
                s = s+tmp[-1-i]
            if int(s)*(-1) < -2147483648:
                return 0
            return int(s)*(-1)

if __name__ == "__main__":
	sol = Solution()
	print(sol.reverse(int(raw_input("Enter the integer to be reversed: "))))
