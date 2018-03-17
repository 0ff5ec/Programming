'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
'''
"""
        :type s: str
        :rtype: str
        """
class Solution(object):
    def isVowel(self, s):
        if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u' or s == 'A' or s == 'E' or s == 'I' or s == 'O' or s == 'U':
            return True
        return False
    def reverseVowels(self, s):
        sol = Solution()
        first_vowel = 0
        last_vowel = len(s) - 1
        reverse = []
        for i in range(len(s)):
            reverse.append(s[i])
        while first_vowel < len(s) and first_vowel < last_vowel:
            if sol.isVowel(reverse[first_vowel]):
                flag = 1
                while last_vowel > first_vowel and flag:
                    if sol.isVowel(reverse[last_vowel]):
                        tmp = reverse[first_vowel]
                        reverse[first_vowel] = reverse[last_vowel]
                        reverse[last_vowel] = tmp
                        flag = 0
                    last_vowel -= 1
            first_vowel += 1
        return ''.join(reverse)

if __name__ == "__main__":
	sol = Solution()
	print(sol.reverseVowels(raw_input('Enter the string: ')))
