#    _*_ coding = utf-8   _*_
'''
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.
'''
"""
        :type s: str
        :rtype: bool
        """
class Solution(object):
    def canPermutePalindrome(self, s):
        dic = {}
        for letter in s:
            if letter in dic.keys():
                dic[letter] += 1
            else:
                dic[letter] = 1
        flag = 0
        for key, value in dic.items():
            if flag > 1:
                return False
            if value%2 == 1:
                flag += 1
        return False if flag > 1 else True

if __name__ == "__main__":
	sol = Solution()
	print(sol.canPermutePalindrome(raw_input('Enter the string: ')))
