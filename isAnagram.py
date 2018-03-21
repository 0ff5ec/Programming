# _*_ coding = utf-8 _*_
'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''
"""
        :type s: str
        :type t: str
        :rtype: bool
        """
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        if sorted(s) == sorted(t):
            return True
        return False

if __name__ == "__main__":
	sol = Solution()
	print(sol.isAnagram(raw_input('Enter string1: '),raw_input('Enter string2: ')))
