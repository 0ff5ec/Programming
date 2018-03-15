'''
Given an integer, write a function to determine if it is a power of two.
'''
"""
        :type n: int
        :rtype: bool
        """
class Solution:
    def isPowerOfTwo(self, n):
        if n<=0:
            return False
        while n != 0:
            tmp = n%2
            if tmp == 1 and n//2 != 0:
                return False
            n = n//2
        return True if tmp == 1 else False

if __name__ == "__main__":
	sol = Solution()
	print(sol.isPowerOfTwo(int(raw_input("Enter the number: "))))
