#   -*-    coding:    utf-8    -*-
'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
'''
"""
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        if len(set(nums)) == len(nums):
            return False
        else:
            dic = {}
            for i in range(len(nums)):
                if str(nums[i]) in dic.keys():
                    if abs(i-dic[str(nums[i])]) <= k:
                        return True
                    else:
                        dic[str(nums[i])] = i
                else:
                    dic[str(nums[i])] = i
            return False

if __name__ == "__main__":
	sol = Solution()
	nums = [1,2,3,4,5,3,2,4,7]
	print(sol.containsNearbyDuplicate(nums,4))
