# _*_ coding = utf-8 _*_
'''
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)
'''
"""
        :type num: int
        :rtype: bool
        """
import math
class Solution(object):
    def checkPerfectNumber(self, num):
        sumFactor = 1
        if num <= 1:
            return False
        else:
            for i in range(2, int(math.sqrt(num))+1):
                if num%i == 0:
                    sumFactor += (i + (num//i))
        return True if sumFactor == num else False

if __name__ == "__main__":
	sol = Solution()
	print(sol.checkPerfectNumber(int(raw_input('Enter the number: '))))
