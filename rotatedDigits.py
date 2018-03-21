# _*_ coding = utf-8 _*_
'''
X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation: 
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
Note:

N  will be in range [1, 10000].
'''
"""
        :type N: int
        :rtype: int
        """
class Solution(object):
    def isRotatedGood(self, num):
        rotatedDic = {'1':1, '2':5, '5':2, '6':9, '8':8, '9':6, '0':0}
        rotated = 0
        n = num
        i = 0
        while num != 0:
            if num%10 == 3 or num%10 == 4 or num%10 == 7:
                return False
            else:
                rotated += (rotatedDic[str(num%10)]*(10**i))
            num = num//10
            i += 1
        return True if rotated != n else False
    def rotatedDigits(self, N):
        sol = Solution()
        cnt = 0
        for i in range(N+1):
            if sol.isRotatedGood(i):
                cnt += 1
        return cnt

if __name__ == "__main__":
	sol = Solution()
	print(sol.rotatedDigits(int(raw_input('Enter the number: '))))
