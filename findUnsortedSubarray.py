#    -*-    coding: utf-8    -*-
'''
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
'''
"""
        :type nums: List[int]
        :rtype: int
        """
class Solution(object):
    def findUnsortedSubarray(self, nums):
        num = sorted(nums)
        start = len(nums)-1
        end = 0
        for i in range(len(nums)):
            num[i] = num[i]^nums[i]
        for i in range(len(num)):
            if num[i] != 0:
                start = i
                break
        for i in range(len(num)-1, -1,-1):
            if num[i] != 0:
                end = i
                break
        return 0 if start >= end else end-start+1

if __name__ == "__main__":
	sol = Solution()
	nums = [1,3,2,4,6,7,5,9,10]
	print(sol.findUnsortedSubarray(nums))
