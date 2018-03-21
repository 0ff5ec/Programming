# _*_ coding = utf-8 _*_
'''
Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.

(Recall that the number of set bits an integer has is the number of 1s present when written in binary. For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)

Example 1:

Input: L = 6, R = 10
Output: 4
Explanation:
6 -> 110 (2 set bits, 2 is prime)
7 -> 111 (3 set bits, 3 is prime)
9 -> 1001 (2 set bits , 2 is prime)
10->1010 (2 set bits , 2 is prime)
Example 2:

Input: L = 10, R = 15
Output: 5
Explanation:
10 -> 1010 (2 set bits, 2 is prime)
11 -> 1011 (3 set bits, 3 is prime)
12 -> 1100 (2 set bits, 2 is prime)
13 -> 1101 (3 set bits, 3 is prime)
14 -> 1110 (3 set bits, 3 is prime)
15 -> 1111 (4 set bits, 4 is not prime)
Note:

L, R will be integers L <= R in the range [1, 10^6].
R - L will be at most 10000.
'''
"""
        :type L: int
        :type R: int
        :rtype: int
        """
class Solution(object):
    def isPrimeSetBits(self, num):
        prime = [2,3,5,7,11,13,17,19]
        setBits = 0
        while num != 0:
            if num%2 == 1:
                setBits += 1
            num = num//2
        return True if setBits in prime else False
    def countPrimeSetBits(self, L, R):
        sol = Solution()
        cnt = 0
        for i in range(L,R+1):
            if sol.isPrimeSetBits(i):
                cnt += 1
        return cnt

if __name__ == "__main__":
	sol = Solution()
	print(sol.countPrimeSetBits(int(raw_input('Enter L: ')), int(raw_input('Enter R: '))))
