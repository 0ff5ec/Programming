# -*- coding: utf-8 -*-
'''
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.
'''
"""
        :type n: int
        :rtype: List[int]
        """
class Solution(object):
    def grayCode(self, n):
        if n <= 0:
            return [0]
        elif n == 1:
            return [0, 1]
        else:
            firstHalf = self.grayCode(n - 1)
            secondHalf = [(1 << (n - 1)) | x for x in reversed(firstHalf)]
            return firstHalf + secondHalf

if __name__ == "__main__":
	sol = Solution()
	print(sol.grayCode(int(raw_input('Enter number of bits: '))))
