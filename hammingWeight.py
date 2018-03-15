'''
Write a function that takes an unsigned integer and returns the number of 1s 
'''
"""
        :type n: int
        :rtype: int
        """
class Solution(object):
    def hammingWeight(self, n):
        ret = 0
        while n != 0:
            tmp = n%2
            if tmp == 1:
                ret += 1
            n = n//2
        return ret

if __name__ == "__main__":
	sol = Solution()
	print(sol.hammingWeight(int(raw_input("Enter the number: "))))
