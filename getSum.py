'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
'''
"""
        :type a: int
        :type b: int
        :rtype: int
        """
class Solution(object):
    def getSum(self, a, b):
        maxInt = 0x7F
        mask = 0xFF
        while b != 0:
            a , b = (a^b)&mask , ((a&b)<<1)&mask
        return a if a <= maxInt else ~(a^mask)

if __name__ == "__main__":
	sol = Solution()
	a,b =3,1
	print(sol.getSum(a,b))
