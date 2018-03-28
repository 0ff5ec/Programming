#    -*- coding: utf-8    -*-
'''
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.
'''
"""
        :type nums: List[int]
        :rtype: List[int]
        """
class Solution(object):
    def findErrorNums(self, nums):
        n = len(nums)
        last = None     
        for index in range(n):
            while nums[index] != nums[nums[index]-1]:
                tmp = nums[index]
                nums[index] = nums[tmp-1]
                nums[tmp-1] = tmp
            if index+1 != nums[index]:
                ans = [nums[index], index+1]
        return ans
        '''dic = {}
        ans = []
        for i in range(1,len(nums)+1):
            dic[i] = 1
        for i in nums:
            if i in dic.keys():
                del dic[i]
            else:
                ans.append(i)
        for k in dic.keys():
            ans.append(k)
        return ans'''

if __name__ == "__main__":
	sol = Solution()
	nums = [1,3,2,2,4]
	print(sol.findErrorNums(nums))
