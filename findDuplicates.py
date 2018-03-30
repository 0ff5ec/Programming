#    -*-    coding: utf-8    -*-
'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
'''
"""
        :type nums: List[int]
        :rtype: List[int]
        """
class Solution(object):
    def findDuplicates(self, nums):
        i = 0
        ans = []
        while i < len(nums):
            if nums[i] != i+1 and nums[i] != nums[nums[i]-1]:
                tmp = nums[i]
                nums[i] = nums[nums[i]-1]
                nums[tmp-1] = tmp
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i+1:
                ans.append(nums[i])
        return sorted(ans)

if __name__ == "__main__":
	sol = Solution()
	nums = [2,2]
	print(sol.findDuplicates(nums))
