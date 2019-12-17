class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        s = ""
        for i in str:
            if ord(i) >64 and ord(i) < 91:
                c = ord(i) + 32
                s += chr(c)
            else:
                s += i
        return s
