#  _*_ coding = utf-8  _*_
'''
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''
"""
        :type s: str
        :rtype: int
        """
class Solution(object):
    def longestPalindrome(self, s):
        if len(s) < 2:
            return len(s)
        dic ={}
        for letter in s:
            if letter in dic.keys():
                dic[letter] += 1
            else:
                dic[letter] = 1
        flag = 0
        lenLongestPal = 0
        if len(dic) == 1:
            return dic[letter]
        for key, value in dic.items():
            if dic[key]%2 == 1:
                flag = 1
            lenLongestPal += dic[key] - dic[key]%2
        return lenLongestPal + 1 if flag else lenLongestPal

if __name__ == "__main__":
	sol = Solution()
	print(sol.longestPalindrome(raw_input('Enter the string: ')))
