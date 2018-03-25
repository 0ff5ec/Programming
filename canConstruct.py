#   -*-   coding:  utf-8   -*-
'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''
"""
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        mag = [l for l in magazine]
        for letter in ransomNote:
            if letter not in mag:
                return False
            elif letter in mag:
                mag.remove(letter)
        return True

if __name__ == "__main__":
	sol = Solution()
	print(sol.canConstruct(raw_input('Enter ransomNote:'),raw_input('Enter magazine: ')))
