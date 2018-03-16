'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''
"""
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
class Solution(object):
    def moveZeroes(self, nums):
        l = len(nums)
        non_zero_index = 0
        i = 0
        while i < l:
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1
            i += 1
        while non_zero_index < l:
            nums[non_zero_index] = 0
            non_zero_index += 1
        return 
        '''for i in range(l-1):
            if nums[i] == 0:
                k = i + 1
                flag = 1
                while k < l and flag:
                    if nums[k] != 0:
                        flag = 0
                        tmp = nums[i]
                        nums[i] = nums[k]
                        nums[k] = tmp
                    k += 1
        return '''

if __name__ == "__main__":
	sol = Solution()
