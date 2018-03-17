'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
'''
"""
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
class Solution(object):
    def intersection(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)
        ret = []
        for i in nums1:
            for j in nums2:
                if i == j:
                    ret.append(i)
        return ret

if __name__ == "__main__":
	sol = Solution()
	nums1 = [1,2,3,4]
	nums2 = [3,4,1]
	print(sol.intersection(nums1,nums2))
