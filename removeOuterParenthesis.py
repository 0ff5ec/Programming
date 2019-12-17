class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        out = ""
        for i in range(len(S)):
            if S[i] == '(':
                stack.append(i)
            else:
                start = stack.pop()
            if not stack and i:
                out += S[start+1:i] 
        return out
