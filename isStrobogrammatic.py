#   -*-   coding: utf-8   -*-
'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.

'''
"""
        :type num: str
        :rtype: bool
        """
class Solution(object):
    def isStrobogrammatic(self, num):
        if num == "":
            return True
        dic = {"1":"1","6":"9","9":"6","8":"8","0":"0"}
        s = ""
        for l in num:
            if l not in dic.keys():
                return False
            s = dic[l] + s
        return True if int(num) == int(s) else False

if __name__ == "__main__":
	sol = Solution()
	print(sol.isStrobogrammatic(raw_input('Enter number: ')))
