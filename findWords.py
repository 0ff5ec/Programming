# _*_ coding = utf-8 _*_
'''
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


American keyboard


Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
'''
"""
        :type words: List[str]
        :rtype: List[str]
        """
class Solution(object):
    def findWords(self, words):
        row1 = "qwertyuiopQWERTYUIOP"
        row2 = "asdfghjklASDFGHJKL"
        row3 = "zxcvbnmZXCVBNM"
        out = []
        for word in words:
            if word[0] in row1:
                i , flag = 0 , 1
                while i<len(word) and flag:
                    if word[i] not in row1:
                        flag = 0
                    i += 1
                if i == len(word) and flag:
                    out.append(word)
            elif word[0] in row2:
                i , flag = 0 , 1
                while i<len(word) and flag:
                    if word[i] not in row2:
                        flag = 0
                    i += 1
                if i == len(word) and flag:
                    out.append(word)
            elif word[0] in row3:
                i , flag = 0 , 1
                while i<len(word) and flag:
                    if word[i] not in row3:
                        flag = 0
                    i += 1
                if i == len(word) and flag:
                    out.append(word)
        return out

if __name__ == "__main__":
	sol = Solution()
	words = ["abdfs","cccd","a","qwwewm"]
	print(sol.findWords(words))
