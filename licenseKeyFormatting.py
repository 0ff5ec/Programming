# _*_ coding = utf-8 _*_
'''
You are given a license key represented as a string S which consists only alphanumeric character and dashes. The string is separated into N+1 groups by N dashes.

Given a number K, we would want to reformat the strings such that each group contains exactly K characters, except for the first group which could be shorter than K, but still must contain at least one character. Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.

Given a non-empty string S and a number K, format the string according to the rules described above.

Example 1:
Input: S = "5F3Z-2e-9-w", K = 4

Output: "5F3Z-2E9W"

Explanation: The string S has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
Example 2:
Input: S = "2-5g-3-J", K = 2

Output: "2-5G-3J"

Explanation: The string S has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
Note:
The length of string S will not exceed 12,000, and K is a positive integer.
String S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9) and dashes(-).
String S is non-empty.
'''
"""
        :type S: str
        :type K: int
        :rtype: str
        """
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        S = S.replace('-', '')[::-1].upper()
        return '-'.join([S[i:i+K] for i in range(0, len(S), K)])[::-1]
        '''l = len(S)   #O(n) Time complexity and O(n) Space complexity
        i = l - 1
        s = ""
        cnt = 0
        while i >= 0:
            if S[i] == "-":
                a = 0
            elif cnt%K == 0 and cnt != 0:
                s = "-" + s
                s = S[i].upper() + s
                cnt = 1
            else:
                s = S[i].upper() + s
                cnt += 1
            i = i - 1
        return s'''
        '''arr = []      #O(2n) Time complexity and O(2n) Space complexity
        for letter in S:
            if letter == "-":
                continue
            else:
                arr.append(letter.upper())
        s = ""
        i = len(arr) - 1
        cnt = 0
        while i>=0:
            if len(s) == 0:
                s = arr[i] + s
            elif cnt%K == 0:
                s = "-" + s
                s = arr[i] + s
            else:
                s = arr[i] + s
            i = i - 1
            cnt += 1
        return s'''

if __name__ == "__main__":
	sol = Solution()
	s = "2-5g-3-J"
	k = 2
	print(sol.licenseKeyFormatting(s,k))
