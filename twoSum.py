'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
"""
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
class Solution:
    def twoSum(self, nums, target):
        a = {}
        for i in range(len(nums)):
            tmp = str(nums[i])
            if tmp in a.keys():
                return [a[tmp], i]
            a[str(target - nums[i])] = i

if __name__ == "__main__":
	nums = [2,7,11,15]
	target = 9
	sol = Solution()
	print(sol.twoSum(nums, target))
