#    -*-    coding : utf-8     -*-
'''
There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.
'''
"""
        :type n: int
        :type k: int
        :rtype: int
        """
class Solution(object):
    def numWays(self, n, k):
        if n == 0:
            return 0
        elif n == 1:
            return k
        diffCol = k*(k-1)
        sameCol = k  
        for i in range(2, n):
            tmp = diffCol
            diffCol = (diffCol + sameCol) * (k-1)
            sameCol = tmp
        return sameCol + diffCol

if __name__ == "__main__":
	sol = Solution()
	print(sol.numWays(int(raw_input('Enter number posts: ')), int(raw_input('Enter number colors: '))))
