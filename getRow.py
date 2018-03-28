#   -*-   coding:utf-8   -*-
'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
'''
"""
        :type rowIndex: int
        :rtype: List[int]
        """
import math
class Solution(object):
    def nCr(self,n,r):
        return math.factorial(n)//math.factorial(r)//math.factorial(n-r)
    def getRow(self, rowIndex):
        ans = []
        for i in range(rowIndex+1):
            ans.append(self.nCr(rowIndex,i))
        return ans

if __name__ == "__main__":
	sol = Solution()
	print(sol.getRow(int(raw_input('Enter row: '))))
