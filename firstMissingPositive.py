'''
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
'''
"""
        :type nums: List[int]
        :rtype: int
        """
class Solution(object):
    def firstMissingPositive(self, nums):
        L = len(nums)
        if L == 0: return 1
        for i in range(L):
            if nums[i] < 0 or nums[i] > L:
                nums[i] = 0
        nums.insert(0, -1)
        for i in range(1, len(nums)):
            int_want_to_visit = nums[i]
            if int_want_to_visit < 0:
                int_want_to_visit = -int_want_to_visit-i
            if nums[int_want_to_visit] >= 0:
                nums[int_want_to_visit] = -nums[int_want_to_visit]-int_want_to_visit
        for i in range(0, len(nums)):
            if nums[i] >= 0: return i
        return len(nums)

if __name__ == "__main__":
	sol = Solution()
	nums = [3,4,-1,1]
	print(sol.firstMissingPositive(nums))
