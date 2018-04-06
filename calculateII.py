#    -*-    coding: utf-8    -*-
'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.
'''
"""
        :type s: str
        :rtype: int
        """
class Solution:
    def calculate(self, s):
        opList, x, operator = [], 0, None
        for i in (s + '+'):
            if ord('0') - 1 < ord(i) < ord('9') + 1: 
                x = x * 10 + ord(i) - ord('0')
            elif i != ' ':
                if operator == '-': x *= -1
                elif operator == '*': x *= opList.pop()
                elif operator == '/': x = int(opList.pop() * 1.0 / x)
                operator = i
                opList.append(x)
                x = 0
        return sum(opList)

if __name__ == "__main__":
	sol = Solution()
	print(sol.calculate(raw_input('Enter the expression: ')))
