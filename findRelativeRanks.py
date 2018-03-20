# _*_ coding = utf-8 _*_
'''
Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according to their scores.
Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.
'''
"""
        :type nums: List[int]
        :rtype: List[str]
        """
class Solution(object):
    def findRelativeRanks(self, nums):
        index = {}
        out = [None]*len(nums)
        for i in range(len(nums)):
            index[str(nums[i])] = i
        sorted_score = sorted(nums)
        for i in range(len(nums)):
            if len(nums) - i == 3:
                out[index[str(sorted_score[i])]] = "Bronze Medal"
            elif len(nums) - i == 2:
                out[index[str(sorted_score[i])]] = "Silver Medal"
            elif len(nums) - i == 1:
                out[index[str(sorted_score[i])]] = "Gold Medal"
            else:
                out[index[str(sorted_score[i])]] = str(len(nums) - i)
        return out

if __name__ == "__main__":
	sol = Solution()
	nums = [237,300,5,719,35]
	print(sol.findRelativeRanks(nums))
