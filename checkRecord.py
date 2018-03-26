#    -*-   coding: utf-8    -*-
'''
You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False
'''
"""
        :type s: str
        :rtype: bool
        """
class Solution(object):
    def checkRecord(self, s):
        absent = 0
        consLate = 0
        i = 0
        while i < len(s):
            if s[i] == "A":
                absent += 1
                if absent > 1:
                    return False
                i += 1
            elif s[i] == "L":
                if i > len(s) - 3:
                    i += 1
                elif s[i+1] == "L" and s[i+2] == "L":
                    return False
                else:
                    i += 1
            else:
                i += 1
        return True

if __name__ == "__main__":
	sol = Solution()
	print(sol.checkRecord(raw_input('Enter attendance record: ')))
