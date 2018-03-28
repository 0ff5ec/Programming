#    -*-    coding: utf-8    -*-
'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
'''
"""
        :type nums: List[int]
        :rtype: int
        """
class Solution(object):
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return -2147483648
        sumList = []
        lSum = 0
        for i in range(1,len(nums)):
            lSum = nums[i-1]+lSum
            if nums[i] <= 0:
                sumList.append(lSum)
            if lSum < 0:
                lSum = 0
        if nums[-1] > 0:
            lSum += nums[-1]
            sumList.append(lSum)
        else:
            sumList.append(nums[-1])
        return sorted(sumList)[-1]

if __name__ == "__main__":
	sol = Solution()
	nums = [1,2,3,-3,-5]
	print(sol.maxSubArray(nums))
