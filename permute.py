#    -*-    coding: utf-8    -*-
'''
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
"""
        :type nums: List[int]
        :rtype: List[List[int]]
        """
class Solution(object):
    def permute(self, nums):
        if len(nums) == 1:
            return [nums]
        result = []
        for i in range(len(nums)):
            tmp = nums[0]
            nums[0] = nums[i]
            nums[i] = tmp
            perm = self.permute(nums[1:])
            for j in perm:
                result.append([nums[0]]+j)
        return result

if __name__ == "__main__":
	sol = Solution()
	nums = [1,2,3,4]
	print(sol.permute(nums))
