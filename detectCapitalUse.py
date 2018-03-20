# _*_ coding = utf-8 _*_
'''
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False
Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
'''
"""
        :type word: str
        :rtype: bool
        """
class Solution(object):
    def detectCapitalUse(self, word):
        if word.upper() == word:
            return True
        elif word[1:].lower() == word[1:]:
            return True
        return False

if __name__ == "__main__":
	sol = Solution()
	print(sol.detectCapitalUse(raw_input('Enter the string: ')))
