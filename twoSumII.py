#   -*-   coding: utf-8   -*-
'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''
"""
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
class Solution(object):
    def twoSum(self, numbers, target):
        low = 0
        high = len(numbers) - 1
        if low == high:
            return [0]
        else:
            while numbers[low]+numbers[high] != target:
                if numbers[low]+numbers[high] > target:
                    high = high - 1
                else:
                    low = low+1
            return [low+1,high+1]

if __name__ == "__main__":
	sol = Solution()
	numbers = [1,2,4,7,9,18]
	target = 20
	print(sol.twoSum(numbers,target))
