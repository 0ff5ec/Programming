#    -*-    coding: utf-8    -*-
'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
'''
"""
        :type n: int
        :rtype: str
        """
class Solution:
    def countAndSay(self, n):
        prev = "1" 
        for i in range(2, n + 1):
            curr_number = prev[0] 
            curr_count = 1 
            result = [] 
            for j in range(1, len(prev)):
                if prev[j] == curr_number:
                    curr_count += 1
                else:
                    result.append(str(curr_count))
                    result.append(curr_number)
                    curr_number = prev[j]
                    curr_count = 1
            result.append(str(curr_count))
            result.append(curr_number)
            prev = "".join(result)
        return prev

if __name__ == "__main__":
	sol = Solution()
	print(sol.countAndSay(int(raw_input('Enter the n: '))))
