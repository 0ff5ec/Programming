# -*- coding: utf-8 -*-
'''
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
Example 2:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.
'''
"""
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
class Solution(object):
    def getMatrix(self, matrix):
        elements = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                elements.append(matrix[i][j])
        return elements
    def matrixReshape(self, nums, r, c):
        sol = Solution()
        if r*c != len(nums)*len(nums[0]):
            return nums
        else:
            elements = sol.getMatrix(nums)
            return [ elements[slice(i*c,c+i*c)] for i in range(r)]
if __name__ == "__main__":
	sol = Solution()
	nums = [[1,2],[3,4]]
	print(sol.matrixReshape(nums,1,4))
