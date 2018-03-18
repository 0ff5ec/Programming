'''
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
'''
"""
        :type nums: List[int]
        :rtype: int
        """
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxCons1s = 0
        tmp = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                maxCons1s = max(tmp, maxCons1s)
                tmp = 0
            else:
                tmp += 1
        return max(maxCons1s,tmp)

if __name__ == "__main__":
	sol = Solution()
	nums = [1,1,0,1,1,1]
	print(sol.findMaxConsecutiveOnes(nums))
