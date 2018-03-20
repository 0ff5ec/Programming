# _*_ coding = utf-8 _*_
'''
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Note:

The boundaries of each input argument are 1 <= left <= right <= 10000.
'''
"""
        :type left: int
        :type right: int
        :rtype: List[int]
        """
class Solution(object):
    def isSelfDividing(self, num):
        n = num
        while n != 0:
            if n%10 == 0:
                return False
            elif num%(n%10) != 0:
                return False
            n = n//10
        return True
    def selfDividingNumbers(self, left, right):
        sol = Solution()
        ans = []
        for i in range(left, right+1):
            if i < 10:
                ans.append(i)
            elif sol.isSelfDividing(i):
                ans.append(i)
        return ans

if __name__ == "__main__":
	sol = Solution()
	print(sol.selfDividingNumbers(int(raw_input('Enter left: ')),int(raw_input('Enter high: '))))
