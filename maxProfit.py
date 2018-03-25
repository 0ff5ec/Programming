#   -*-   coding:  utf-8   -*-
'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''
"""
        :type prices: List[int]
        :rtype: int
        """
class Solution(object):
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

if __name__ == "__main__":
	sol = Solution()
	prices = [1,2,3,4,5]
	print(sol.maxProfit(prices))
