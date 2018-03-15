'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''
"""
        :type n: int
        :rtype: bool
        """
class Solution(object):
    def sqrDigitSum(self, n):
        ans = 0
        while n!= 0:
            ans = ans + (n%10)**2
            n = n//10
        return ans
    def isHappy(self, n):
        sol = Solution()
        loop_check = []
        while sol.sqrDigitSum(n) != 1:
            if sol.sqrDigitSum(n) in loop_check:
                return False
            loop_check.append(sol.sqrDigitSum(n))
            n = sol.sqrDigitSum(n)
        return True

if __name__ == "__main__":
	sol = Solution()
	print(sol.isHappy(int(raw_input("Enter the number: "))))
