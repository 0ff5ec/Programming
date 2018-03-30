#    -*-    coding: utf-8    -*_
'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''
"""
        :type nums: List[int]
        :rtype: List[int]
        """
class Solution(object):
    def findDisappearedNumbers(self, nums):
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
                ans.append(i+1)
        return ans

if __name__ == "__main__":
	sol = Solution()
	nums = [2,2]
	print(sol.findDisappearedNumbers(nums))
