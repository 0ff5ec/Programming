#    -*-    coding: utf-8    -*-
'''
We are given non-negative integers nums[i] which are written on a chalkboard.  Alice and Bob take turns erasing exactly one number from the chalkboard, with Alice starting first.  If erasing a number causes the bitwise XOR of all the elements of the chalkboard to become 0, then that player loses.  (Also, we'll say the bitwise XOR of one element is that element itself, and the bitwise XOR of no elements is 0.)

Return True if and only if Alice wins the game, assuming both players play optimally.

Example:
Input: nums = [1, 1, 2]
Output: false
Explanation: 
Alice has two choices: erase 1 or erase 2. 
If she erases 1, the nums array becomes [1, 2]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 2 = 3. Now Bob can remove any element he wants, because Alice will be the one to erase the last element and she will lose. 
If Alice erases 2 first, now nums becomes [1, 1]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 1 = 0. Alice will lose.

Notes:

0 <= N <= 1000. 
0 <= nums[i] <= 2^16.
'''
"""
        :type nums: List[int]
        :rtype: bool
        """
class Solution(object):
    def xorCal(self,nums):
        totalXor = 0
        for i in nums:
            totalXor ^= i
        return totalXor
    def xorGame(self, nums):
        if len(nums) == 0:
            return True
        if len(nums) == 1:
            return False
        xor = self.xorCal(nums)
        if xor == 0:
            return True
        l = len(nums)
        for i in range(len(nums)):
            if xor^nums[i]:
                xor = xor^nums[i]
                nums = nums[:i]+nums[i+1:]
                break
        if l == len(nums):
            xor = xor^nums[0]
            nums = nums[1:]
        return True if not self.xorGame(nums) else False

if __name__ == "__main__":
	sol = Solution()
	nums = [1,2,3]
	if sol.xorGame(nums):
		print('Alice wins')
	else:
		print('Alice loses')
