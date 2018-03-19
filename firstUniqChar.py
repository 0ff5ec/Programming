'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''
"""
        :type s: str
        :rtype: int
        """
class Solution(object):
    def firstUniqChar(self, s):
        let_dict = {}
        del_dict = {}
        for i in range(len(s)):
            if s[i] in let_dict.keys():
                del let_dict[s[i]]
                del_dict[s[i]] = True
            elif s[i] not in del_dict.keys():
                let_dict[s[i]] = i
        ret = []
        if not let_dict:
            return -1
        for k,v in let_dict.items():
            ret.append(v)
        return min(ret)

if __name__ == "__main__":
	sol = Solution()
	print(sol.firstUniqChar(raw_input("Enter the string: ")))
