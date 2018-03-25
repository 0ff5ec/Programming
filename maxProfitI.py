#   -*-    coding:   utf-8   -*-
'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
'''
"""
        :type prices: List[int]
        :rtype: int
        """
class Solution(object):
    def maxProfit(self, prices):
        minStock = 200000000
        maxProfit = 0
        for i in range(len(prices)):
            if prices[i] < minStock:
                minStock = prices[i]
            elif prices[i] - minStock > maxProfit:
                maxProfit = prices[i] - minStock
        return maxProfit

if __name__ == "__main__":
	sol = Solution()
	prices = [1,2,3,4,5]
	print(sol.maxProfit(prices))
