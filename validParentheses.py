'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''
"""
        :type s: str
        :rtype: bool
        """
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
class Solution:
    def isValid(self, s):
        para_dict = {')':'(','}':'{',']':'['}
        sol = Stack()
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                sol.push(s[i])
            elif s[i] == ')' or s[i] == '}' or s[i] == ']':
                if sol.isEmpty():
                    return False
                else:
                    if sol.pop() != para_dict[s[i]]:
                        return False
        return True if sol.isEmpty() else False
if __name__ == "__main__":
	sol = Solution()
	print(sol.isValid(raw_input("Enter the string with parentheses: ")))
