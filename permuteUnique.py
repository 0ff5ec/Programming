#    -*-    coding: utf-8    -*-
'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''
"""
        :type nums: List[int]
        :rtype: List[List[int]]
        """
class Solution(object):
    def permuteUnique(self, nums):
        if len(nums) == 1:
            return [nums]
        result = []
        for i in range(len(nums)):
            tmp = nums[0]
            nums[0] = nums[i]
            nums[i] = tmp
            perm = self.permuteUnique(nums[1:])
            for j in perm:
                if [nums[0]]+j not in result:
                    result.append([nums[0]]+j)
        return result

if __name__ == "__main__":
	sol = Solution()
	nums = [1,3,2,1,1,6]
	print(sol.permuteUnique(nums))
