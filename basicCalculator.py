# -* coding: utf-8 *-
'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
'''
class Solution:
    def calculate(self, s):
        sol = Solution()
        ans = 0
        operands = []
        operator = []
        pivot = 0
        i = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
                continue
            elif s[i].isnumeric():
                j = i+1
                tmp = s[i]
                while j<len(s) and s[j].isnumeric():
                    tmp = tmp+s[j]
                    j += 1
                    continue
                operands.append(int(tmp))
                i = j
            elif s[i] == "+":
                if s[i+1] == "+":
                    operator.append("+")
                    i += 2
                elif s[i+1] == "-":
                    operator.append("-")
                    i += 2
                else:
                    operator.append(s[i])
                    i += 1
            elif s[i] == "-":
                if s[i+1] == "+":
                    operator.append("-")
                    i += 2
                elif s[i+1] == "-":
                    operator.append("+")
                    i += 2
                else:
                    operator.append(s[i])
                    i += 1
            elif s[i] == "(":
                pivot = i
                i += 1
            elif s[i] == ")":
                s1 = s[:pivot]
                if s[pivot+1:i].isnumeric():
                    s2 = s[pivot+1:i]
                else:
                    s2 = str(sol.calculate(s[pivot+1:i]))
                s3 = s[i+1:]
                i += 1
                try:
                    return int(s1+s2+s3)
                except:
                    return sol.calculate(s1+s2+s3)
                #else:
                    #return sol.calculate(s1+s2+s3)
        #print(operands)
        #print(operator)
        for i in range(len(operator)):
            if operator[i] == "+":
                operands[i+1] = operands[i] + operands[i+1]
            else:
                operands[i+1] = operands[i] - operands[i+1]
        return operands[-1]
"""
        :type s: str
        :rtype: int
        """

if __name__ == "__main__":
	sol = Solution()
	s = u"(1+(4+5+2)-3)+(6+8)"
	print(sol.calculate(s))
