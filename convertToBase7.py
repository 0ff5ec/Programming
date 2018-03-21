# _*_ coding = utf-8 _*_
'''
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].
'''
"""
        :type num: int
        :rtype: str
        """
class Solution(object):
    def convertToBase7(self, num):
        if num == 0:
            return "0"
        s = ""
        n = abs(num)
        while n != 0:
            s = str(n%7) + s
            n = n//7
        return s if num >= 0 else "-"+s

if __name__ == "__main__":
	sol = Solution()
	print(sol.convertToBase7(int(raw_input('Enter the number: '))))
