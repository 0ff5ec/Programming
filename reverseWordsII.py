#    -*-    coding: utf-8    -*-
'''
Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Could you do it in-place without allocating extra space?

Related problem: Rotate Array

Update (2017-10-16):
We have updated the function signature to accept a character array, so please reset to the default code definition by clicking on the reload button above the code editor. Also, Run Code is now available!

'''
"""
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
class Solution:
    def reverse(self, s, i, j):
        while i < j:
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i += 1
            j -= 1
        return
    def reverseWords(self, str):
        self.reverse(str,0,len(str)-1)
        i = 0
        j = len(str)
        k = 0
        while i < j:
            if i == j-1:
                self.reverse(str,k,i)
            if str[i] == " ":
                self.reverse(str,k,i-1)
                k = i+1
            i += 1
        return
        '''l = len(str)
        str = "".join(str).split(" ")
        n = len(str)
        for i in range(len(str)//2):
            tmp = str[i]
            str[i] = str[n-1-i]
            str[n-1-i] = tmp
        str = " ".join(str)
        for i in range(l):
            print(str[i])'''

if __name__ == "__main__":	
	sol = Solution()
	print(sol.reverseWords(input('Enter string: ')))
