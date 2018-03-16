'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
"""
        :type numRows: int
        :rtype: List[List[int]]
        """
class Solution(object):
    def generate(self, numRows):
        ans = [[1], [1,1]]
        p1 = [1]
        p2 = [1,1]
        if numRows == 0:
            return []
        if numRows == 1:
            return [p1]
        if numRows == 2:
            return [p1,p2]
        prev = [1,1]
        k = 2
        while k < numRows:
            new = [None]*(k+1)
            for i in range(1,len(prev)):
                new[0] , new[-1] = 1, 1
                new[i]  = prev[i-1] + prev[i]
            prev = new
            ans.append(prev)
            k += 1
        return ans

if __name__ == "__main__":
	sol = Solution()
	print(sol.generate(int(raw_input("Enter the number: "))))
