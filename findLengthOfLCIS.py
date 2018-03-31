#    -*-    coding: utf-8    -*-
'''
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
Note: Length of the array will not exceed 10,000.
'''
"""
        :type nums: List[int]
        :rtype: int
        """
class Solution(object):
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0
        longest = 1
        l = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                l += 1
            else:
                longest = max(longest,l)
                l = 1
        return max(longest,l)

if __name__ == "__main__":
	sol = Solution()
	nums = [5,2,1,2,5,3,2,8]
	print(sol.findLengthOfLCIS(nums))
