'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
'''
"""
        :type num: int
        :rtype: int
        """
class Solution(object):
    def addDigits(self, num):
        if num < 10:
            return num
        strN = str(num)
        ans = 0
        for i in strN:
            ans = ans + int(i)
            if ans > 9:
                ans -= 9
        return ans

if __name__ == "__main__":
	sol = Solution()
	print(sol.addDigits(int(raw_input("Enter the number: "))))
