'''
There are 1000 buckets, one and only one of them contains poison, the rest are filled with water. They all look the same. If a pig drinks that poison it will die within 15 minutes. What is the minimum amount of pigs you need to figure out which bucket contains the poison within one hour.

Answer this question, and write an algorithm for the follow-up general case.

Follow-up:

If there are n buckets and a pig drinking poison will die within m minutes, how many pigs (x) you need to figure out the "poison" bucket within p minutes? There is exact one bucket with poison.
'''
"""
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
import math
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        return int(math.ceil(math.log(buckets)/math.log(minutesToTest/minutesToDie+1)))

if __name__ == "__main__":
	sol = Solution()
	buckets = 1000
	minutesToTest , minutesToDie = 60 , 15
	print(sol.poorPigs(buckets, minutesToDie, minutesToTest))
