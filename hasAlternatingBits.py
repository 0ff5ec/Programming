# _*_ coding = utf-8 _*_
'''
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.
Example 3:
Input: 11
Output: False
Explanation:
The binary representation of 11 is: 1011.
Example 4:
Input: 10
Output: True
Explanation:
The binary representation of 10 is: 1010.
'''
"""
        :type n: int
        :rtype: bool
        """
class Solution(object):
    def hasAlternatingBits(self, n):
        prev = None
        while n != 0:
            if prev == None:
                prev = n%2
            elif prev == n%2:
                return False
            prev = n%2
            n = n//2
        return True

if __name__ == "__main__":
	sol = Solution()
	print(sol.hasAlternatingBits(int(raw_input('Enter the number: '))))
