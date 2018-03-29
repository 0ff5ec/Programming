#   -*- coding: utf-8   -*-
'''
Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".

Note:
Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

Example 1:
Given s = "internationalization", abbr = "i12iz4n":

Return true.
Example 2:
Given s = "apple", abbr = "a2e":

Return false.
'''
"""
        :type word: str
        :type abbr: str
        :rtype: bool
        """
class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        if len(abbr) > len(word):
            return False
        num = 0
        numL = 0
        i = 0
        while i < len(abbr):
            if not abbr[i].isalpha():
                if abbr[i] == "0":
                    return False
                j = i + 1
                while j < len(abbr):
                    if abbr[j].isalpha():
                        break
                    j += 1
                num += int(abbr[i:j])
                numL += j-i
                i += j-i
            elif abbr[i].isalpha():
                if i + num - numL > len(word)-1:
                    return False
                if abbr[i] != word[i+num-numL]:
                    return False
                i += 1
        return True if len(abbr) + num - numL == len(word) else False

if __name__ == "__main__":
	sol = Solution()
	print(sol.validWordAbbreviation(raw_input('Enter word: '),raw_input('Enter abbr: ')))
