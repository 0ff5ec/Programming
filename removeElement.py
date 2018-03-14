'''
Given an array and a value, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.
'''
"""
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
class Solution:
    def removeElement(self, nums, val):
        cnt = 0
        i , j = 0 , len(nums)
        while i != j:
            if nums[i] == val:   
                nums.remove(nums[i])
                nums.append(val)
                j = j-1
                cnt += 1
            else:
                i = i+1
        return len(nums) - cnt
if __name__ == "__main__":
	nums = [3,2,2,3]
	val = 3
	sol = Solution()
	print(sol.removeElement(nums,val))
