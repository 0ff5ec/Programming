# -*- coding: utf-8 -*-
'''
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''
"""
        :type nums: List[int]
        :rtype: int
        """
class Solution(object):
    def thirdMax(self, nums):
        if len(nums) < 3:
            return max(nums) if len(nums) > 0 else -1
        threeMax = [nums[0]]
        i = 1
        while i < len(nums):
            if nums[i] not in threeMax:
                if len(threeMax) < 3:
                    threeMax.append(nums[i])
                    threeMax.sort()
                else:
                    if nums[i] > min(threeMax):
                        threeMax[0] = nums[i]
                        threeMax.sort()
            i += 1
        if len(threeMax) < 3:
            return max(threeMax)
        else:
            return min(threeMax)

if __name__ == "__main__":
	sol = Solution()
	nums = [6,2,1,9,-1]
	print(sol.thirdMax(nums))
