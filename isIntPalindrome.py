'''
Determine whether an integer is a palindrome. Do this without extra space.
'''
"""
        :type x: int
        :rtype: bool
        """
class Solution:
    def isPalindrome(self, x):
        x = str(x)
        l = len(x)
        for i in range(len(x)):
            if x[i] != x[l-1-i]:
                return False
        return True

if __name__ == "__main__":
	sol = Solution()
	print(sol.isPalindrome(int(raw_input("Enter an integer you want to check: "))))
