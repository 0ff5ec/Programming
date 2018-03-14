'''
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
'''
"""
        :type n: int
        :rtype: int
        """
class Solution:
    def trailingZeroes(self, n):
        ans = 0
        if n<5:
            return 0
        i = 5
        while n//i != 0:
            ans = ans + n//i
            i = 5*i
        return ans

if __name__ == "__main__":
	sol = Solution()
	print(sol.trailingZeroes(int(raw_input("Enter the number: "))))
