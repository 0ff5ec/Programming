#  _*_ coding = utf-8 _*_ 
'''
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
'''
"""
        :type cost: List[int]
        :rtype: int
        """
class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = min(cost[i] + dp[i-1], cost[i] + dp[i-2])
        ans = min(dp[n-1], dp[n-2])
        return ans

if __name__ == "__main__":
	sol = Solution()
	nums = [0,0,0,1]
	print(sol.minCostClimbingStairs(nums))
