#   -*-    coding: utf-8    -*-
'''
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
'''
"""
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
class Solution(object):
    def rotate(self, nums, k):
        i = 0
        while i < k:
            nums.insert(0,nums.pop())
            i += 1

if __name__ == "__main__":
	sol = Solution()
	nums = [1,2,3,4,5,6,7,8,9]
	k = 4
	print(sol.rotate(nums,k))
