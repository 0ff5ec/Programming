'''
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
'''
"""
        :type digits: List[int]
        :rtype: List[int]
        """
class Solution:
    def plusOne(self, digits):
        if digits[-1] != 9:
            digits[-1] = digits[-1] + 1
            return digits
        i = -1
        flag = 1
        while i > (-len(digits)-1) and flag:
            tmp = digits[i]
            digits[i] = (tmp+1)%10
            if (tmp+1)//10 == 0:
                flag = 0
            i = i-1
        if flag:
            digits = [1] + digits
        return digits

if __name__ == "__main__":
	sol = Solution()
	digits = [9,9,9]
	print(sol.plusOne(digits))
