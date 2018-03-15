'''
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
'''
"""
        :type n: int
        :rtype: int
        """

class Solution(object):
    def findNthDigit(self, n):
        c = 9
        if n//c == 0:
            return n
        i = 2
        sub = 0
        while n//c != 0:
            n = n - c
            sub += c//(i-1)
            c = (10**(i-1))*i*9
            i = i+1
        i = i - 1
        if n/(1.0*i) == n//i:
            num = n//i + sub
        else:
            num = n//i + sub + 1
        rem = n%i
        return int(str(num)[rem-1])

if __name__ == "__main__":
	sol = Solution()
	print(sol.findNthDigit(int(raw_input("Enter the N: "))))
