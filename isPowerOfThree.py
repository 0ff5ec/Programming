'''
Given an integer, write a function to determine if it is a power of three.
'''
"""
        :type n: int
        :rtype: bool
        """
class Solution:
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        while n != 0:
            tmp = n%3
            if tmp !=0 and n//3 != 0:
                return False
            n = n//3
        return True if tmp == 1 else False

if __name__ == "__main__":
	sol = Solution()
	print(sol.isPowerOfThree(int(raw_input("Enter the number: "))))
