'''Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
'''
"""
        :type num: int
        :rtype: bool
        """
class Solution(object):
    def isUgly(self, num):
        if num == 1:
            return True
        if num == 0:
            return False
        n = num
        while n%2 == 0:
            n = n//2
            if n == 1:
                return True
        while n%3 == 0:
            n = n//3
            if n == 1:
                return True
        while n%5 == 0:
            n = n//5
            if n == 1:
                return True
        return True if n == 1 else False

if __name__ == "__main__":
	sol = Solution()
	print(sol.isUgly(int(raw_input("Enter the number: "))))
